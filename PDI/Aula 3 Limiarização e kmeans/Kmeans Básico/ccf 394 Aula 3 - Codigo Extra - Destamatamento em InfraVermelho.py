import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import cv2
from PIL import Image



def process_image_cir(im, area_km2):
    # Converte a imagem para numpy array
    im = np.array(im)
    
    # Tamanho da imagem e contagem de pixels
    rows, cols, _ = im.shape
    print (rows,cols)
    pixel_count = rows * cols
    pixel_area_km2 = area_km2 / pixel_count

    plt.figure()
    plt.imshow(im)
    plt.title("Imagem original")
    plt.show()

    # Separar camadas CIR
    nir = im[:, :, 0]
    red = im[:, :, 1]
    green = im[:, :, 2]
    imagem = np.hstack([nir,red,green])
    #imagem = cv2.resize(imagem, cols//4, rows//4)

    # Ajuste de contraste no RED e GREEN
    red = cv2.normalize(red, None, 0, 255, cv2.NORM_MINMAX)
    green = cv2.normalize(green, None, 0, 255, cv2.NORM_MINMAX)

    # Construção da imagem CIR
    cir = np.stack((nir, red, green), axis=-1)

    plt.figure()
    plt.imshow(cir)
    plt.title("Após ajuste de contraste no RED e GREEN")
    plt.show()

    # Filtro gaussiano
    nir = cv2.GaussianBlur(nir, (5,5), 0.8)
    red = cv2.GaussianBlur(red, (5,5), 0.8)
    green = cv2.GaussianBlur(green, (5,5), 0.8)

    cir = np.stack((nir, red, green), axis=-1)

    # K-Means
    K = 3

    # Reorganiza para passar ao k-means
    cir_reshaped = cir.reshape((rows * cols, 3))
    kmeans = KMeans(n_clusters=K, random_state=0).fit(cir_reshaped)
    labeled = kmeans.labels_.reshape((rows, cols))

    # Plot da segmentação
   
    # Plot da segmentação
    labeled_rgb = np.zeros((rows, cols, 3), dtype=np.uint8)  # Criando um array RGB de 3 canais
    for i in range(K):
        labeled_rgb[labeled == i] = np.array([255, 0, 0], dtype=np.uint8)  # Atribuindo cor para cada cluster



    plt.figure()
    plt.imshow(labeled_rgb)
    plt.title('Imagem segmentada. Clique em uma área de floresta')
    plt.show()

    # Pede ao usuário para clicar em uma área de floresta
    print("Escolha uma área de floresta na imagem...")

    # Após clique, você pode usar o índice do ponto para calcular a área correspondente
    # Supondo que o usuário clique em um ponto específico (a posição de floresta é determinada)
    y, x = 100, 100  # Definido manualmente aqui. Altere conforme a interação do usuário
    label_floresta = labeled[y, x]

    # Calcular área
    areas = np.array([np.sum(labeled == i) * pixel_area_km2 for i in range(K)])
    
    floresta_km2 = areas[label_floresta]
    floresta_pct = (floresta_km2 / area_km2) * 100
    
    return floresta_km2, floresta_pct



# Carregar as imagens
im_old = Image.open("candeias_junho_2017_cir.png")
im_new = Image.open("candeias_nov_2022_cir.png")

area_km2 = 1.243

# Processamento CIR
print("\n================ CIR =================")
area_old, pct_old = process_image_cir(im_old, area_km2)
area_new, pct_new = process_image_cir(im_new, area_km2)

print(f"Área analisada = {area_km2:.4f} km^2 \t({100:.2f}%)")
print("--------------------------------------")
print("Floresta")
print("--------------------------------------")
print(f"Antigo  : Área = {area_old:.4f} km^2 \t({pct_old:.2f}%)")
print(f"Novo    : Área = {area_new:.4f} km^2 \t({pct_new:.2f}%)")
print(f"Diff    : Área = {area_new - area_old:.4f} km^2 \t({pct_new - pct_old:.2f}%)")
