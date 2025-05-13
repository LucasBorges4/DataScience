import cv2
import numpy as np

# Carrega a imagem
imagem = cv2.imread('plantioCana.jpg')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Converte para HSV para segmentar a copa verde
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Máscara para tons de verde (ajuste se necessário)
verde_min = np.array([30, 40, 40])
verde_max = np.array([85, 255, 255])
mascara_verde = cv2.inRange(hsv, verde_min, verde_max)

# --- PASSA-MÉDIA: Suavização na copa ---
imagem_suavizada = imagem.copy()
suavizada_copa = cv2.blur(imagem, (15, 15))
imagem_suavizada[mascara_verde > 0] = suavizada_copa[mascara_verde > 0]

# --- PASSA-BAIXA: Detecção de bordas com Sobel na copa ---
# Converte para escala de cinza
cinza = cv2.cvtColor(imagem_suavizada, cv2.COLOR_BGR2GRAY)

# Aplica filtro Sobel apenas na região das copas
sobelx = cv2.Sobel(cinza, cv2.CV_64F, 1, 0, ksize=3)  # gradiente x
sobely = cv2.Sobel(cinza, cv2.CV_64F, 0, 1, ksize=3)  # gradiente y

# Calcula a magnitude do gradiente
magnitude = cv2.magnitude(sobelx, sobely)
magnitude = cv2.convertScaleAbs(magnitude)

# Aplica a máscara verde
bordas_sobel_copa = cv2.bitwise_and(magnitude, magnitude, mask=mascara_verde)

# Mostra os resultados
cv2.imshow("Original", imagem)
cv2.imshow("Copa Suavizada", imagem_suavizada)
cv2.imshow("Bordas (Sobel nas Copas)", bordas_sobel_copa)
cv2.waitKey(0)
cv2.destroyAllWindows()
