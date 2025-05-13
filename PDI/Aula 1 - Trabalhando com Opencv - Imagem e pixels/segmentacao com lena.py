import cv2
import numpy as np

def atualizar_limiar(valor):
    _, img_bin = cv2.threshold(img_cinza, valor, 255, cv2.THRESH_BINARY)
    img_colorida = cv2.bitwise_and(img_original, img_original, mask=img_bin)
    cv2.imshow("Imagem Binária", img_bin)
    cv2.imshow("Imagem Colorida", img_colorida)

# Carregar a imagem
img_original = cv2.imread("lena.jpg")
img_cinza = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# Criar janela e trackbar
cv2.namedWindow("Segmentação")
cv2.createTrackbar("Limiar", "Segmentação", 0, 255, atualizar_limiar)

# Mostrar a imagem original em tons de cinza
cv2.imshow("Segmentação", img_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
