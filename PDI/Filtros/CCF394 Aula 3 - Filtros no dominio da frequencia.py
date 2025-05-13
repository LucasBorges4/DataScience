"""



Comandos Básicos para o Procedimento de filtragem
img=double(img) --> Converte a imagem para a classe double
fft2 ---> Transformada de fourier do domínio espacial para o domínio das frequencias
fftshift ---> Inverte os quadrantes da imagem no domínio das frequencias.
img .* filtro---> Multiplica pixel por pixel pontualmente (.) pelo filtro (Operação de Filtragem)
fftshift ---> Re-inverte os quadrantes da imagem no domínio das frequencias.
ifft2 ---> Transformada inversa de fourier do domínio das frequencias para o domínio espacial
img=uint8(img) --> Converte a imagem para a classe double
imshow(img) ---> Mostra a imagem na tela
figure ---> Abre mais uma janela para novas figuras
Dica: Sempre que tiver dúvias sobre o funcionamento de determinada função, digite na linha de
comando help "função"
(ex: help fft2, help imshow)





"""



import numpy as np
import cv2
from matplotlib import pyplot as plt
#img = cv2.imread("lena_impulsiva.png",0)
img = cv2.imread("lena_impulsiva.png",0)

img_float32 = np.float32(img)
# discrete_fourier_transform dft
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
#Shift the zero-frequency component to the center of the spectrum.
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


#criando uma mascara no centro da imagem do espectro de frequecia,
# gerando um filtro passa baixa.
rows, cols = img.shape
crow, ccol = (rows/2 , cols/2)     # center
crow=np.uint(crow)
ccol=np.uint(ccol)

#cria a macara com o centro 1m 1, o resto é 0
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# aplica a mascara e o inverso da fft
fshift = dft_shift*mask

f_ishift = np.fft.ifftshift(fshift)
#invero dft
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(141),plt.imshow(img, cmap = 'gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(142),plt.imshow(img_back, cmap = 'gray')
plt.title('Imagem Filtrada'), plt.xticks([]), plt.yticks([])

plt.subplot(143),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Espectro imagem original'), plt.xticks([]), plt.yticks([])

img_float32 = np.float32(img_back)
# discrete_fourier_transform dft
dft2 = cv2.dft(np.float32(img_back),flags = cv2.DFT_COMPLEX_OUTPUT)
#Shift the zero-frequency component to the center of the spectrum.
dft_shift2 = np.fft.fftshift(dft2)
magnitude_spectrum2 = 20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))

plt.subplot(144),plt.imshow(magnitude_spectrum2, cmap = 'gray')
plt.title('Espectro imagem filtrada'), plt.xticks([]), plt.yticks([])
plt.show()



 
