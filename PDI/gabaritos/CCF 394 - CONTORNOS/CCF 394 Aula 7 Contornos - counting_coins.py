#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="coins.jpg", help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = image.copy()
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

# Supondo que `gray` é sua imagem em escala de cinza
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradiente horizontal
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradiente vertical

# Calcula a magnitude do gradiente
sobel_mag = np.sqrt(sobelx**2 + sobely**2)

# Normaliza e converte para uint8
sobel_mag = np.uint8(255 * sobel_mag / np.max(sobel_mag))

# Opcional: aplicar um limiar para simular a saída binária do Canny
_, edged = cv2.threshold(sobel_mag, 50, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 1), np.uint8)
edged = cv2.erode(edged, kernel)
cv2.imshow("Edge Detection", np.hstack([gray,edged]))
cv2.waitKey(0)
(cnts, hierarquia) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
coins = image.copy()
moedas =0
# Exiba a imagem com o contorno preenchido
for (i, c) in enumerate (cnts):
    # Calcula a área do contorno
    area = cv2.contourArea(c)
    # Verifica se a área é maior que 200
    if area > 1000:
        moedas=moedas+1
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.drawContours(coins, c, -1, 255, thickness=cv2.FILLED)
print(f"Quantidade de moedas: {moedas}")
cv2.imshow("Contornos", coins)
cv2.waitKey(0)

