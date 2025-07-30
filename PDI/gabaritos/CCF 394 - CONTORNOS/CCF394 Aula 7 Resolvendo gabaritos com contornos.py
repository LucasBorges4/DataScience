import cv2
import numpy as np

def ajustar_recorte(imagem):
    """Recorta a maior área contornada da imagem, assumindo que seja o gabarito."""
    imgGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 150)

    contornos, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contornos:
        print("Nenhum contorno encontrado!")
        return imagem

    maior = max(contornos, key=cv2.contourArea)
    epsilon = 0.02 * cv2.arcLength(maior, True)
    aprox = cv2.approxPolyDP(maior, epsilon, True)

    if len(aprox) == 4:
        # Reordena pontos para perspectiva
        pontos = np.array([p[0] for p in aprox], dtype='float32')
        pontos = ordenar_pontos(pontos)

        largura, altura = 500, 600
        destino = np.array([[0,0], [largura,0], [0,altura], [largura,altura]], dtype='float32')

        matriz = cv2.getPerspectiveTransform(pontos, destino)
        recortada = cv2.warpPerspective(imagem, matriz, (largura, altura))
        return recortada
    else:
        print("Contorno principal não tem 4 lados! Retornando imagem original.")
        return imagem

def ordenar_pontos(pts):
    """Ordena os 4 pontos no formato: topo-esquerda, topo-direita, baixo-esquerda, baixo-direita."""
    soma = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    ordenado = np.zeros((4, 2), dtype="float32")
    ordenado[0] = pts[np.argmin(soma)]       # Topo-esquerda
    ordenado[3] = pts[np.argmax(soma)]       # Baixo-direita
    ordenado[1] = pts[np.argmin(diff)]       # Topo-direita
    ordenado[2] = pts[np.argmax(diff)]       # Baixo-esquerda

    return ordenado

def rotacionar_imagem(img, angulo):
    """Roda a imagem em torno do centro."""
    (h, w) = img.shape[:2]
    centro = (w // 2, h // 2)
    matriz_rotacao = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    imagem_rotacionada = cv2.warpAffine(img, matriz_rotacao, (w, h), flags=cv2.INTER_LINEAR)
    return imagem_rotacionada

# Configurações do grid
num_questoes = 5
num_alternativas = 4  # A, B, C, D

respostasCorretas = ["1-A", "2-C", "3-B", "4-D", "5-A"]
opcoes = ['A', 'B', 'C', 'D']

#Nome do arquivo de imagem
# Se a imagem estiver em outro diretório, forneça o caminho completo
image_name = 'gab5.png'
if not image_name:
    print("Nome da imagem não fornecido.")
    exit()
# Carrega imagem
imagem = cv2.imread(image_name)
if imagem is None:
    print(f"Erro ao carregar a imagem: {image_name}")
    exit()
    
# Ajusta recorte
    
imagem = ajustar_recorte(imagem)
imagem = cv2.resize(imagem, (500, 600))

imagem = rotacionar_imagem(imagem, 0)

altura_img, largura_img = imagem.shape[:2]
gabarito = imagem.copy()

# Pré-processamento
imgGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
_, imgTh = cv2.threshold(imgGray, 10, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)
imgTh = cv2.dilate(imgTh, kernel, iterations=2)

# Tamanho das células
cell_h = altura_img // num_questoes
cell_w = largura_img // num_alternativas

respostas = []
for i in range(num_questoes):
    for j in range(num_alternativas):
        x = j * cell_w
        y = i * cell_h
        w = cell_w
        h = cell_h

        # Desenha grid
        cv2.rectangle(gabarito, (x, y), (x + w, y + h), (0, 0, 255), 1)

        # Verifica marcação
        campo = imgTh[y:y + h, x:x + w]
        total = campo.shape[0] * campo.shape[1]
        pretos = cv2.countNonZero(campo)
        percentual = round((pretos / total) * 100, 2)

        if percentual >= 15:
            cv2.rectangle(gabarito, (x, y), (x + w, y + h), (255, 0, 0), 2)
            resposta = f"{i+1}-{opcoes[j]}"
            respostas.append(resposta)

# Correção
acertos = 0
erros = 0
if len(respostas) == len(respostasCorretas):
    for i, res in enumerate(respostas):
        if res == respostasCorretas[i]:
            print(f'{res} Verdadeiro, correto: {respostasCorretas[i]}')
            acertos += 1
        else:
            print(f'{res} Falso, correto: {respostasCorretas[i]}')
            erros += 1

    cv2.putText(imagem, f'ACERTOS: {acertos}, PONTOS: {acertos}', (30, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

print(f'Quantidade de acertos: {acertos}')
print(f'Quantidade de erros: {erros}')

# Mostra resultados
cv2.imshow('Imagem', imagem)
cv2.imshow('Gabarito com Grid', gabarito)
cv2.imshow('Threshold com Dilation', imgTh)
cv2.waitKey(0)
cv2.destroyAllWindows()
