import cv2
import numpy as np
import os

# --- Funções auxiliares ---

def ordenar_pontos(pts):
    soma = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)
    ordenado = np.zeros((4, 2), dtype="float32")
    ordenado[0] = pts[np.argmin(soma)]       # topo-esquerda
    ordenado[3] = pts[np.argmax(soma)]       # baixo-direita
    ordenado[1] = pts[np.argmin(diff)]       # topo-direita
    ordenado[2] = pts[np.argmax(diff)]       # baixo-esquerda
    return ordenado

def ajustar_recorte(imagem):
    """Recorta e endireita a maior área contornada (presume o gabarito)."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1)
    canny = cv2.Canny(blur, 50, 150)
    cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return imagem
    maior = max(cnts, key=cv2.contourArea)
    eps = 0.02 * cv2.arcLength(maior, True)
    aprox = cv2.approxPolyDP(maior, eps, True)
    if len(aprox) == 4:
        pts = np.array([p[0] for p in aprox], dtype="float32")
        pts = ordenar_pontos(pts)
        w, h = 500, 600
        dst = np.array([[0,0],[w,0],[0,h],[w,h]], dtype="float32")
        M = cv2.getPerspectiveTransform(pts, dst)
        return cv2.warpPerspective(imagem, M, (w,h))
    else:
        return imagem

# --- Configurações gerais ---

respostas_corretas = ["1-B", "2-C", "3-B", "4-D", "5-A"]
num_questoes = 5
num_alternativas = 4
opcoes = ['A','B','C','D']

# Lista de arquivos de entrada
imagens = [f"gab{i}.png" for i in range(1,7)]

# Cria pasta de saída
os.makedirs("corrigidos", exist_ok=True)

# --- Loop de processamento ---

for img_name in imagens:
    img = cv2.imread(img_name)
    if img is None:
        print(f"Não foi possível carregar {img_name}")
        continue

    # 1) Recorte e alinhamento
    img = ajustar_recorte(img)
    img = cv2.resize(img, (500,600))

    # cópias para desenho
    corrigido = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3), np.uint8)
    th = cv2.dilate(th, kernel, iterations=2)

    h, w = img.shape[:2]
    cell_h = h // num_questoes
    cell_w = w // num_alternativas

    respostas_detectadas = []

    # 1) Primeiro desenha todos os quadrados vermelhos e pontos centrais
    for i in range(num_questoes):
        for j in range(num_alternativas):
            x, y = j*cell_w, i*cell_h
            # retângulo vermelho (por baixo do círculo verde)
            cv2.rectangle(corrigido, (x, y), (x+cell_w, y+cell_h), (0,0,255), 5)
            # ponto vermelho no centro
            cx, cy = x + cell_w//2, y + cell_h//2
            cv2.circle(corrigido, (cx, cy), 50, (0,0,255), -1)

            # checa preenchimento para detectar resposta
            sub = th[y:y+cell_h, x:x+cell_w]
            total = sub.size
            pretos = cv2.countNonZero(sub)
            if (pretos/total)*100 >= 15:
                respostas_detectadas.append(f"{i+1}-{opcoes[j]}")

    # 2) Destaca respostas marcadas com contorno preto e cor verde/vermelha dependendo da correção
    raio_marcado = int(min(cell_w, cell_h) * 0.4)

    for resposta in respostas_detectadas:
        q, alt_marcada = resposta.split('-')
        q = int(q)
        correta = respostas_corretas[q - 1].split('-')[1]
        idx = opcoes.index(alt_marcada)
        x, y = idx * cell_w, (q - 1) * cell_h
        cx, cy = x + cell_w // 2, y + cell_h // 2

        if alt_marcada == correta:
            cor = (0, 255, 0)  # Verde para acerto
        else:
            cor = (0, 0, 255)  # Vermelho para erro

        # Desenha borda preta
        cv2.circle(corrigido, (cx, cy), raio_marcado + 5, (0, 0, 0), -1)  # Preenche o fundo preto
        cv2.circle(corrigido, (cx, cy), raio_marcado, cor, -1)           # Círculo colorido por cima
        cv2.putText(corrigido, alt_marcada, (cx - 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 1)
    # 3) Pinta de verde toda a área das respostas corretas
    # Aqui usamos o mesmo 'raio_marcado' para o círculo de preenchimento
    for rc in respostas_corretas:
        q, alt = rc.split('-')
        q = int(q) - 1
        idx = opcoes.index(alt)
        x, y = idx * cell_w, q * cell_h
        cx, cy = x + cell_w//2, y + cell_h//2

        # círculo verde preenchido sobre a célula correta
        cv2.circle(corrigido, (cx, cy), raio_marcado, (0, 255, 0), -1)

    # salva e mostra
    out_name = os.path.join("corrigidos", f"corrigido_{img_name}")
    cv2.imwrite(out_name, corrigido)
    cv2.imshow(f"Corrigido {img_name}", corrigido)

cv2.imshow("Threshold", th)
cv2.waitKey(0)
cv2.destroyAllWindows()
