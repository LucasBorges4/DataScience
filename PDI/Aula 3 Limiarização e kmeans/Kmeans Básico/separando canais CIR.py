ara separar as bandas de uma imagem CIR (Color Infrared), que é composta por três bandas (normalmente, NIR, RED e GREEN), você pode acessar as diferentes bandas no formato de matriz da imagem. As imagens CIR geralmente têm as seguintes associações de bandas:

NIR (Infravermelho próximo): Esta banda é normalmente armazenada no primeiro canal da imagem (no caso de uma imagem RGB, geralmente no canal vermelho).

RED (Vermelho): Esta banda é armazenada no segundo canal da imagem (geralmente no canal verde).

GREEN (Verde): Esta banda é armazenada no terceiro canal da imagem (geralmente no canal azul).

Exemplo de como separar as bandas de uma imagem CIR usando Python:
python
Copiar
Editar
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Carregar a imagem CIR (exemplo: uma imagem RGB)
image = Image.open('caminho_da_imagem.png')

# Converter a imagem para um array NumPy
image_array = np.array(image)

# Separar as bandas (assumindo que a imagem é RGB, com NIR no canal 0, RED no canal 1, GREEN no canal 2)
nir = image_array[:,:,0]  # Banda NIR
red = image_array[:,:,1]  # Banda RED
green = image_array[:,:,2]  # Banda GREEN

# Exibir as bandas separadas
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(nir, cmap='gray')
plt.title('Banda NIR')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(red, cmap='gray')
plt.title('Banda RED')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(green, cmap='gray')
plt.title('Banda GREEN')
plt.axis('off')

plt.tight_layout()
plt.show()
