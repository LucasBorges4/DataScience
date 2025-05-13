import cv2
import numpy as np
repeticoes = 7;  #/ Repetitions for strong cartoon effect.
smallImg=cv2.imread("imagens/biel.png")
(b,g,r)= cv2.split(smallImg)
maxB=np.max((b))
b=b+(255-np.max(b))

cv2.imshow("cartoon",smallImg)
tmp=smallImg.copy()

ksize = 7;     # Filter size. Has a large effect on speed.
sigmaColor = 7;    # Filter color strength.
sigmaSpace = 7;    # Spatial strength. Affects speed.
tmpB=cv2.bilateralFilter(b,  ksize, sigmaColor, sigmaSpace);
tmpG=cv2.bilateralFilter(g,  ksize, sigmaColor, sigmaSpace);
tmpR=cv2.bilateralFilter(r,  ksize, sigmaColor, sigmaSpace);

for i in range (0,repeticoes):
  
  tmpB=cv2.bilateralFilter(tmpB, ksize, sigmaColor, sigmaSpace);
  tmpG=cv2.bilateralFilter(tmpG, ksize, sigmaColor, sigmaSpace);
  tmpR=cv2.bilateralFilter(tmpR, ksize, sigmaColor, sigmaSpace);

imagem=cv2.merge((tmpB,tmpG,tmpR))
cv2.imshow("cartoon",imagem)
cv2.waitKey(0)
