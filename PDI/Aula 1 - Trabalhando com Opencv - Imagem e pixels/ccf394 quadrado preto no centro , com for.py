import cv2

# Carregar a imagem
imagem = cv2.imread("lena.jpg")

# Obter dimensões da imagem
altura, largura, canais = imagem.shape

# Definir dimensões do quadrado
quadrado_largura = largura // 2
quadrado_altura = altura // 2

# Calcular coordenadas do canto superior esquerdo do quadrado
x1 = (largura - quadrado_largura) // 2
y1 = (altura - quadrado_altura) // 2

# Percorrer os pixels dentro da região do quadrado e pintar de preto
for y in range(y1, y1 + quadrado_altura):
    for x in range(x1, x1 + quadrado_largura):
        imagem[y, x] = (0, 0, 0)  # Define o pixel como preto

# Exibir e salvar a imagem
cv2.imshow("Imagem com Quadrado Preto", imagem)
cv2.imwrite("imagem_modificada.jpg", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

