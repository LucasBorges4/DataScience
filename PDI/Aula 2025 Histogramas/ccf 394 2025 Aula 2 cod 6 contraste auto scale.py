import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
image = cv.imread("wiki.png",cv.IMREAD_GRAYSCALE)
print(image.shape)
min=np.min(image)
max=np.max(image)
print(max,min)
new_image = np.zeros(image.shape, image.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
         new_image[y,x] = np.uint8(10+255*((image[y,x]-min)/(max-min)))
min=np.min(new_image)
max=np.max(new_image)
print(max,min)
plt.subplot(221), plt.imshow(image,cmap='gray')
plt.subplot(222), plt.imshow(new_image,cmap='gray')

plt.subplot(223)
plt.hist(image.ravel(),256,[0,256]),
plt.title('Histograma para uma imagem em tons de cinza')
plt.subplot(224)
plt.hist(new_image.ravel(),256,[0,256])
plt.title('aplicando uma transformacao linear')

plt.show()
cv.waitKey(0)

cv.destroyAllWindows()
