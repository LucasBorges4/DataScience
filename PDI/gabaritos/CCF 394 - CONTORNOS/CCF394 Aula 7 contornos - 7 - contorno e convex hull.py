import cv2
import numpy as np

# Carrega a imagem 'maoaberta.png' e exibe-a em uma janela com o título "original"
image = cv2.imread('maoaberta.png')
cv2.imshow("original", image)

# Converte a imagem para tons de cinza
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica o algoritmo Canny para detecção de bordas
canny_img = cv2.Canny(img_gray, 30, 200)

# Encontra os contornos na imagem binarizada
contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Lembrando que -1 plota todos os contornos

# Desenha os contornos encontrados na imagem original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
#cv2.imshow("contorno",image)
#cv2.waitKey(0)
# Inicializa uma nova imagem carregando novamente a imagem original
image2 = cv2.imread('maoaberta.png')

# Itera sobre os contornos encontrados
for c in contours:
    # Calcula o casco convexo para cada contorno
    convexHull = cv2.convexHull(c)
    # Desenha o casco convexo na imagem2
    cv2.drawContours(image2, [convexHull], -1, (255, 0, 0), 2)
    # Calcula os defeitos de convexidade
    hull = cv2.convexHull(c, returnPoints=False)
    defects = cv2.convexityDefects(c, hull)

    # Itera sobre os defeitos de convexidade encontrados
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(c[s][0])
        end = tuple(c[e][0])
        far = tuple(c[f][0])
        # Desenha uma linha entre o início e o fim do defeito
        cv2.line(image2, start, end, [0, 255, 0], 2)
        # Desenha um círculo no ponto de defeito
        cv2.circle(image2, far, 5, [0, 0, 255], -1)

# Exibe a imagem2 com o casco convexo e os defeitos de convexidade
ambas = np.hstack((image,image2))
cv2.imshow('ConvexHull', ambas)
cv2.waitKey(0)

# Salva a imagem2 como 'teste.png'
cv2.imwrite("teste.png", image2)

# Fecha todas as janelas abertas
cv2.destroyAllWindows()
