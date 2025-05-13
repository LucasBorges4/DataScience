import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_multiotsu
'''
Otsu Multinível (Multilevel Otsu Thresholding)
A variação multinível do método de Otsu generaliza o critério de minimização da variância intraclasse para mais de dois limiares, dividindo a imagem em várias classes C1,C2,...Cn
Objetivo: Encontrar k limiaries, t1,t2,...tk   que maximizem a separação das k+1 classes da imagem.

Critério: A função objetivo é maximizar a soma das variâncias interclasses, similar à abordagem do Otsu clássico.


Liao, P-S., Chen, T-S. and Chung, P-C., “A fast algorithm for multilevel thresholding”,
Journal of Information Science and Engineering 17 (5): 713-727, 2001.
Available at: <https://ftp.iis.sinica.edu.tw/JISE/2001/200109_01.pdf>.
'''
# Carregar imagem e converter para escala de cinza
imagem = data.camera()

# Aplicar limiarização multinível usando o Otsu com 3 classes
limiares = threshold_multiotsu(imagem, classes=3)

# Segmentar a imagem com os limiares encontrados
imagem_segmentada = np.digitize(imagem, bins=limiares)

# Mostrar resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")

plt.subplot(1, 3, 2)
plt.hist(imagem.ravel(), bins=256)
plt.axvline(limiares[0], color='r', linestyle='--', label=f'Limiar 1: {limiares[0]}')
plt.axvline(limiares[1], color='g', linestyle='--', label=f'Limiar 2: {limiares[1]}')
plt.title("Histograma com Limiarização")
plt.legend()

plt.subplot(1, 3, 3)
plt.imshow(imagem_segmentada, cmap='jet')
plt.title("Imagem Segmentada")

plt.show()
