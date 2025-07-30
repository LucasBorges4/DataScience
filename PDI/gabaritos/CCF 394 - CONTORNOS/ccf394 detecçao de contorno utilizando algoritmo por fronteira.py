import cv2
import numpy as np

# Carregar e binarizar imagem
img = cv2.imread('maoaberta.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
binary = cv2.dilate(binary, kernel, iterations=1)
# Dimensões da imagem
h, w = binary.shape

# Direções para os 8 vizinhos (sentido horário)
directions = [(-1, -1), (0, -1), (1, -1), (1, 0),
              (1, 1), (0, 1), (-1, 1), (-1, 0)]

def dentro(x, y):
    return 0 <= x < w and 0 <= y < h

def encontrar_contorno(img_bin):
    contorno = []
    visitado = np.zeros_like(img_bin, dtype=bool)

    # Encontrar o primeiro pixel branco (255)
    for y in range(h):
        for x in range(w):
            if img_bin[y, x] == 255 and not visitado[y, x]:
                atual = (x, y)
                start = atual
                contorno.append(atual)
                visitado[y, x] = True
                dir_ant = 7  # direção inicial arbitrária

                while True:
                    achou = False
                    # Começar a busca a partir da direção anterior
                    for i in range(8):
                        idx = (dir_ant + i) % 8
                        dx, dy = directions[idx]
                        nx, ny = atual[0] + dx, atual[1] + dy

                        if dentro(nx, ny) and img_bin[ny, nx] == 255 and not visitado[ny, nx]:
                            atual = (nx, ny)
                            contorno.append(atual)
                            visitado[ny, nx] = True
                            dir_ant = (idx + 5) % 8  # novo ponto, nova direção base
                            achou = True
                            break
                    if not achou or atual == start:
                        break
                return contorno
    return contorno

# Aplicar detecção de contorno
contorno = encontrar_contorno(binary)

# Desenhar contorno
output = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
for i in range(len(contorno)):
    cv2.circle(output, contorno[i], 1, (0, 255, 0), -1)

# Mostrar resultado
cv2.imshow("Contorno por algoritmo de fronteira", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
