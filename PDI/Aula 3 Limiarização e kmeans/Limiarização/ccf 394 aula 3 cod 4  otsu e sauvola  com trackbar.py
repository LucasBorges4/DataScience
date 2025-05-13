import cv2
import numpy as np

def sauvola_threshold(img, window_size=15, k=0.2, R=128):
    # Calcula a média e o desvio padrão em uma janela deslizante
    mean = cv2.boxFilter(img, cv2.CV_64F, (window_size, window_size))
    sqmean = cv2.boxFilter(img ** 2, cv2.CV_64F, (window_size, window_size))
    variance = sqmean - mean ** 2

    # Corrigir possíveis valores negativos e adicionar uma pequena constante para evitar divisão por zero
    variance = np.maximum(variance, 0)
    stddev = np.sqrt(variance + 1e-8)

    # Calcula o threshold de Sauvola
    sauvola_thresh = mean * (1 + k * ((stddev / R) - 1))

    # Aplica o threshold para gerar a imagem binária
    binarized = (img > sauvola_thresh).astype(np.uint8) * 255
    return binarized

def on_trackbar(val):
    threshold_value = cv2.getTrackbarPos("Threshold", window_name)

    # Aplicando o threshold manualmente usando o valor ajustado
    _, manual_thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Aplicando o threshold de Otsu automaticamente
    _, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplicando o threshold de Sauvola personalizado
    sauvola_thresh = sauvola_threshold(gray)


    # Mostrando o resultado lado a lado
    combined = np.hstack((manual_thresh, otsu_thresh, sauvola_thresh))
    cv2.imshow(window_name, combined)

# Carregar uma imagem em escala de cinza
image = cv2.imread("sudoku.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro ao carregar a imagem!")
    exit()

gray = cv2.GaussianBlur(image, (5, 5), 0)  # Aplicar blur para remover ruído

window_name = "Limiarizacao: Manual x Otsu x Sauvola"
cv2.namedWindow(window_name)

# Criar o trackbar para ajustar o limiar manualmente
cv2.createTrackbar("Threshold", window_name, 0, 255, on_trackbar)

# Inicializar o trackbar no meio
cv2.setTrackbarPos("Threshold", window_name, 128)

on_trackbar(128)  # Mostrar a imagem inicial com threshold 128

cv2.waitKey(0)
cv2.destroyAllWindows()
