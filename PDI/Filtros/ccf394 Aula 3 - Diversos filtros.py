import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("imagens/lena_impulsiva.png")
kernel = np.array( [[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])
filter2d = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
cv2.imshow("janela",filter2d)
cv2.waitKey()

# Define os filtros
media = np.array([[0.1111, 0.1111, 0.1111],
                  [0.1111, 0.1111, 0.1111],
                  [0.1111, 0.1111, 0.1111]])

gauss = np.array([[0.0625, 0.125, 0.0625],
                  [0.125, 0.25, 0.125],
                  [0.0625, 0.125, 0.0625]])

horizontal = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])

vertical = np.array([[-1, -2, -1],
                     [0, 0, 0],
                     [1, 2, 1]])

laplacian = np.array([[0, -1, 0],
                      [-1, 4, -1],
                      [0, -1, 0]])

boost = np.array([[0, -1, 0],
                  [-1, 5.2, -1],
                  [0, -1, 0]])

# Carrega a imagem
image_path = "imagens/lena_impulsiva.png"  # Substitua pelo caminho da sua imagem
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Aplica os filtros
filtered_media = cv2.filter2D(image, -1, media)
filtered_gauss = cv2.filter2D(image, -1, gauss)
filtered_horizontal = cv2.filter2D(image, -1, horizontal)
filtered_vertical = cv2.filter2D(image, -1, vertical)
filtered_laplacian = cv2.filter2D(image, -1, laplacian)
filtered_boost = cv2.filter2D(image, -1, boost)

# Exibe as imagens usando Matplotlib com subplot 3x3
plt.figure(figsize=(12, 10))

plt.subplot(3, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(filtered_media, cmap='gray')
plt.title('Filtered with Media Filter')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(filtered_gauss, cmap='gray')
plt.title('Filtered with Gauss Filter')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(filtered_horizontal, cmap='gray')
plt.title('Filtered with Horizontal Filter')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(filtered_vertical, cmap='gray')
plt.title('Filtered with Vertical Filter')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(filtered_laplacian, cmap='gray')
plt.title('Filtered with Laplacian Filter')
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(filtered_boost, cmap='gray')
plt.title('Filtered with Boost Filter')
plt.axis('off')

plt.tight_layout()
plt.show()

# Aguarda até que o usuário pressione a tecla 'Esc' para sair
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Tecla 'Esc'
        break

cv2.destroyAllWindows()
