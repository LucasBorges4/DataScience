import cv2
import matplotlib.pyplot as plt
import numpy as np
#Para exibir uma única imagem:
#showImages([img1], ["Título 1"], size=(10,10), grid=(1,1))

#Para exibir duas imagens lado a lado:
#showImages([img1, img2], ["Título 1", "Título 2"], size=(10,10), grid=(1,2))

#Para exibir quatro imagens em uma grade 2x2:
#showImages([img1, img2, img3, img4], ["Título 1", "Título 2", "Título 3", "Título 4"], size=(10,10), grid=(2,2))

def showImages(imgsArray, titlesArray, size, grid=(1,1)):
    y, x = grid
    fig, axes = plt.subplots(y, x, figsize=size)
    axes = axes.ravel() if isinstance(axes, np.ndarray) else np.array([axes])

    if len(imgsArray) != len(titlesArray):
        print("ERRO: O número de imagens e títulos deve ser o mesmo!")
        return

    for idx, (img, title) in enumerate(zip(imgsArray, titlesArray)):
        if len(img.shape) == 2:  # A imagem é tons de cinza
            axes[idx].imshow(img, cmap='gray')
        else:  # A imagem é RGB
            axes[idx].imshow(img)
        axes[idx].set_title(title, fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
        if len(title) == 0:
            axes[idx].axis('off')

    plt.tight_layout()  # ajusta automaticamente o layout para evitar sobreposição
    plt.show()
    
# Carrega a imagem em escala de cinza
image = cv2.imread('wiki.png', 0)

# Realiza a equalização do histograma
equ = cv2.equalizeHist(image)

# Exiba as imagens antes e depois da equalização do histograma
showImages([image, equ], ['Original', 'Imagem Equalizado'], size=(7,4), grid=(1,2))
# Calcule o histograma da imagem original e da imagem equalizada
hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])

# Exiba os histogramas
plt.figure()
plt.title('Histogramas')
plt.xlabel('Intensidade de cor')
plt.ylabel('Número de pixels')

# Plotando cada histograma
plt.plot(hist_image, color='b', label='Original')
plt.plot(hist_equ, color='r', label='Equalizado')

plt.legend()
plt.xlim([0, 256])
plt.show()
