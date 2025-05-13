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
    


# Carregar a imagem
image = cv2.imread('lena.jpg')

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calcular o histograma
'''
[gray_image]: Este é o primeiro argumento da função e é uma lista das imagens de entrada. 
Aqui, você está passando uma lista contendo apenas uma imagem (gray_image).

[0]: Este é o segundo argumento e representa os canais de cores para os quais o histograma é calculado. 
No caso de imagens em tons de cinza, o valor é [0] porque só há um canal. 
Se a imagem fosse colorida e se quisesse calcular o histograma para todos os canais de cores, 
passaria [0, 1, 2].

None: Este é o terceiro argumento e representa a máscara. 
Se você passar uma máscara, o histograma será calculado apenas para os pixels da imagem que estão mascarados.
Aqui, é passado None, o que significa que o histograma é calculado para toda a imagem.

[256]: Este é o quarto argumento e representa o número de bins no histograma. 
Um bin é um intervalo de valores de intensidade e cada bin conta o número de pixels na imagem que têm 
valores de intensidade dentro desse intervalo. 
Aqui, é passado [256], o que significa que será criado um histograma com 256 bins. 
Portanto, cada bin corresponderá a um valor de intensidade diferente na imagem, variando de 0 a 255.

[0, 256]: Este é o quinto argumento e representa o intervalo de valores de intensidade. 
Aqui, você passou [0, 256], o que significa que está calculando o histograma para todas as cores, 
de 0 a 255. 
Se quisesse calcular o histograma apenas para um subconjunto específico de valores, passaria um 
intervalo diferente.
'''
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plotar o histograma
plt.figure()
plt.title("Histograma de escala de cinza")
plt.xlabel("Bins")
plt.ylabel("# de Pixels")
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()

# Calcular o histograma para cada canal de cor
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color = color)
    plt.xlim([0, 256])

plt.title("Histograma colorido")
plt.xlabel("Bins")
plt.ylabel("# de Pixels")
plt.show()
# Divida a imagem em canais B, G e R
B, G, R = cv2.split(image)

# Agora, B, G e R são imagens monocromáticas correspondentes aos canais azul, 
# verde e vermelho da imagem original.
showImages([B, G, R], ["Banda B", "Banda G", "Banda R"], size=(8, 8), grid=(3,1))
