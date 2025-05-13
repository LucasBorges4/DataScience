import cv2
import numpy as np
# Carregar a imagem
imagem = cv2.imread("lena.jpg")
# Obter dimensões da imagem
altura, largura, _ = imagem.shape
# Definir dimensões do quadrado
quadrado_largura = largura // 2
quadrado_altura = altura // 2
# Calcular coordenadas do canto superior esquerdo e inferior direito do quadrado
x1 = (largura - quadrado_largura) // 2
y1 = (altura - quadrado_altura) // 2
x2 = x1 + quadrado_largura
y2 = y1 + quadrado_altura
# Desenhar o quadrado preto
imagem[y1:y2, x1:x2] = (0, 0, 0)



# Exibir e salvar a imagem

cv2.imshow("Imagem com Quadrado Preto", imagem)

cv2.imwrite("imagem_modificada.jpg", imagem)

cv2.waitKey(0)

cv2.destroyAllWindows()
