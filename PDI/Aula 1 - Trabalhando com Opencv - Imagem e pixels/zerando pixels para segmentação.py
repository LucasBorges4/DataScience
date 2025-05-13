import cv2
import numpy as np

# Carregar a imagem em escala de cinza
imagem = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# Definir os pixels menores que 100 como 0
imagem[imagem < 150] = 0

# Mostrar a imagem resultante
cv2.imshow('Imagem Resultante', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
