import cv2
import random
import string
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import win32api




# Define o tamanho da imagem
altura, largura = 20, 20

# Define o número de imagens a serem geradas para cada letra
num_imagens = 10

# Define o caminho para salvar as imagens geradas
caminho = './dataset/'
# Testa se o caminho existe
if not os.path.exists(caminho):
    # Cria o caminho
    os.makedirs(caminho)


# Define os tipos de fonte a serem usados

# diretório onde as fontes estão instaladas
font_dir = "C:\\Windows\\Fonts"

# lista todos os arquivos na pasta de fontes
font_files = os.listdir(font_dir)

# filtra apenas os arquivos de fontes TrueType (.ttf)
tipos_fonte = [f for f in font_files if f.endswith('.ttf')]



# Percorre cada letra do alfabeto
for letra in string.ascii_uppercase:

    # Percorre o número de imagens a serem geradas para cada letra
    for i in range(num_imagens):

        # Escolhe aleatoriamente uma fonte e uma variação de itálico e negrito
        tipo_fonte = random.choice(tipos_fonte)
       

        # Define o nome da fonte com base na escolha aleatória
        nome_fonte = tipo_fonte

        # Define o tamanho da fonte
        tamanho_fonte = 20

        # Define a cor do texto
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Cria uma imagem em branco com o tamanho definido
        imagem = Image.new(mode='RGB', size=(largura, altura), color='white')

        # Cria um objeto Draw a partir da imagem
        draw = ImageDraw.Draw(imagem)

        # Cria um objeto Font a partir da fonte e tamanho definidos
        fonte = ImageFont.truetype(font="C:\\Windows\\Fonts\\"+nome_fonte , size=tamanho_fonte)

        # Desenha a letra na imagem usando a fonte e cor definidas
        draw.text((0, 0), letra, font=fonte, fill=cor_texto)

        # Converte a imagem para um array numpy
        imagem = np.array(imagem, dtype=np.uint8)

        # Salva a imagem no disco com o nome do arquivo no formato "LETRA_XXX.jpg"
        nome_arquivo = letra + '_' + nome_fonte + '_' + str(i).zfill(3) + '.jpg'
        cv2.imwrite(caminho + nome_arquivo, imagem)

