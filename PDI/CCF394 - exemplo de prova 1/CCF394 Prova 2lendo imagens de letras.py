import os
from PIL import Image
import pandas as pd

# Crie um dataframe vazio
df = pd.DataFrame(columns=['nome_imagem', 'classe'])

# Defina o caminho para a pasta de imagens
caminho = './dataset/'

# Crie uma lista para armazenar as novas linhas
novas_linhas = []

# Percorra todos os arquivos da pasta
for arquivo in os.listdir(caminho):
    print(arquivo)

    # Verifique se o arquivo é do tipo jpg
    if arquivo.endswith('.jpg'):

        # Carregue a imagem usando a biblioteca Pillow
        imagem = Image.open(os.path.join(caminho, arquivo))

        # Extraia a primeira letra do nome da imagem como classe
        classe = arquivo[0]

        # Adicione um dicionário representando a nova linha à lista
        novas_linhas.append({'nome_imagem': arquivo, 'classe': classe})

# Concatene todas as novas linhas ao dataframe existente
df = pd.concat([df, pd.DataFrame(novas_linhas)], ignore_index=True)

# Imprima o dataframe resultante
print(df)
