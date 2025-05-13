import cv2
import matplotlib.pyplot as plt

# Caminho da imagem (substitua pelo caminho da sua imagem)
caminho_imagem = 'IMAGENS\AVIAO.jpg'

# Lê a imagem
imagem = cv2.imread(caminho_imagem)

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
    exit()

# Converte de BGR para RGB para exibir corretamente com matplotlib
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Aplica filtros de média com diferentes tamanhos de kernel
kernels = [3, 5, 7, 9, 11]
imagens_filtradas = [cv2.blur(imagem_rgb, (k, k)) for k in kernels]

# Mostra as imagens usando matplotlib
plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(imagem_rgb)
plt.title('Original')
plt.axis('off')

for i, (img, k) in enumerate(zip(imagens_filtradas, kernels)):
    plt.subplot(2, 3, i+2)
    plt.imshow(img)
    plt.title(f'Média {k}x{k}')
    plt.axis('off')

plt.tight_layout()
plt.show()