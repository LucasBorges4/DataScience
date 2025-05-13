import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('imagens/biel.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Suaviza com filtro gaussiano (passa-baixa)
blurred = cv2.GaussianBlur(img_rgb, (9, 9), 0)

# Converte para escala de cinza para detecção de bordas
gray = cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY)

# Detecta bordas com filtro Laplaciano (passa-alta)
edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
_, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

# Aplica a máscara nas regiões suavizadas
cartoon = cv2.bitwise_and(blurred, blurred, mask=mask)

# Exibe o resultado
cv2.imshow('Cartoon Gaussiano + Laplaciano', cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()



# Suavização com filtro bilateral (preserva bordas)
smooth = cv2.bilateralFilter(img_rgb, d=9, sigmaColor=75, sigmaSpace=75)

# Bordas com Canny
edges = cv2.Canny(smooth, 100, 150)
edges_inv = cv2.bitwise_not(edges)

# Combina imagem suavizada com bordas
cartoon = cv2.bitwise_and(smooth, smooth, mask=edges_inv)

cv2.imshow('Cartoon Bilateral + Canny', cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()







from scipy.ndimage import generic_filter

def harmonic_mean_filter(img_gray, size=5):
    return generic_filter(img_gray.astype(np.float32), harmonic, size=(size, size)).astype(np.uint8)


def harmonic(p):
    eps = 1e-8
    return len(p) / np.sum(1.0 / (p + eps))

# Escala de cinza
gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# Suavização com média harmônica
harmonic = harmonic_mean_filter(gray, size=5)
harmonic_color = cv2.cvtColor(harmonic, cv2.COLOR_GRAY2RGB)

# Detecção de bordas com Sobel
sobelx = cv2.Sobel(harmonic, cv2.CV_8U, 1, 0, ksize=5)
sobely = cv2.Sobel(harmonic, cv2.CV_8U, 0, 1, ksize=5)
sobel = cv2.bitwise_or(sobelx, sobely)
_, mask = cv2.threshold(sobel, 80, 255, cv2.THRESH_BINARY_INV)

# Combina
cartoon = cv2.bitwise_and(harmonic_color, harmonic_color, mask=mask)

cv2.imshow('Cartoon Harmônica + Sobel', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
