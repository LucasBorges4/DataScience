import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('menina.png')

# Define o valor do parâmetro gamma (normalmente entre 0,1 e 5)
gamma1 = 1.3

# Aplica a correção gama na imagem
img_corrigida1 = np.power(img/255.0, gamma1)
img_corrigida1 = np.uint8(img_corrigida1*255)


gamma2 = 0.6
# Aplica a correção gama na imagem
img_corrigida2 = np.power(img/255.0, gamma2)
img_corrigida2 = np.uint8(img_corrigida2*255)


# Mostra as imagens original e corrigida lado a lado
imagem_lado_a_lado = np.hstack((img, img_corrigida1,img_corrigida2))
cv2.imshow('Imagem Original e duas correcoes (gama de 1,3  e 0,6) ', imagem_lado_a_lado)
cv2.waitKey(0)
# Fecha a janela
cv2.destroyAllWindows()
