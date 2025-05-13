import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
image = cv.imread("wiki.png",cv.IMREAD_GRAYSCALE)
# use 1.3 e 40 como entrada
min=np.min(image)
max=np.max(image)
print(max,min)
# um deslocamento de 20 na imagem
nova=(image+20)*(255/(max-min))
nova=np.uint8(nova)
print(np.max(nova),np.min(nova))
plt.subplot(221), plt.imshow(image,cmap='gray')
plt.subplot(222), plt.imshow(nova,cmap='gray')
plt.subplot(223), plt.hist(image.ravel(),256,[0,256]),plt.title('Histograma ')
plt.subplot(224), plt.hist(nova.ravel(),256,[0,256]),plt.title('transformacao linear')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

# agora, lendo os valores de contraste e brilho do teclado g(x) =alfa*f(x)  + betaa
new_image = np.zeros(image.shape, image.dtype)
alpha = 1.0 # Simple contrast control
beta = 0    # Simple brightness control
# Initialize values
print(' Transformação linear basica ')
print('-------------------------')
try:
    alpha = float(input('* Entre com alpha (contraste) [1.0-3.0]: '))
    beta = int(input('* Entre com  beta (brilho) [0-100]: '))
except ValueError:
    print('Error, not a number')
# new_image(i,j) = alpha*image(i,j) + beta

new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)

plt.subplot(221), plt.imshow(image,cmap='gray')
plt.subplot(222), plt.imshow(new_image,cmap='gray')

plt.subplot(223), plt.hist(image.ravel(),256,[0,256]),plt.title('Histograma para uma imagem em tons de cinza')
plt.subplot(224), plt.hist(new_image.ravel(),256,[0,256]),plt.title('aplicando uma transformacao linear')

plt.show()
cv.waitKey(0)


cv.waitKey()
cv.destroyAllWindows()
