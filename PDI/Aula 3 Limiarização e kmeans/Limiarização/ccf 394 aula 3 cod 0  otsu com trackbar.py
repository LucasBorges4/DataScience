import cv2
import numpy as np

def on_trackbar(val):
    threshold_value = cv2.getTrackbarPos("Threshold", window_name)

    # Aplicando o threshold manualmente usando o valor ajustado
    _, manual_thresh = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Aplicando o threshold de Otsu automaticamente
    _, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Mostrando o resultado lado a lado
    combined = np.hstack((manual_thresh, otsu_thresh))
    cv2.imshow(window_name, combined)

# Carregar uma imagem em escala de cinza
image = cv2.imread("sudoku.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro ao carregar a imagem!")
    exit()


window_name = "Limiarizacao: Manual x Otsu"
cv2.namedWindow(window_name)

# Criar o trackbar para ajustar o limiar manualmente
cv2.createTrackbar("Threshold", window_name, 0, 255, on_trackbar)

# Inicializar o trackbar no meio
cv2.setTrackbarPos("Threshold", window_name, 128)

on_trackbar(128)  # Mostrar a imagem inicial com threshold 128

cv2.waitKey(0)
cv2.destroyAllWindows()
