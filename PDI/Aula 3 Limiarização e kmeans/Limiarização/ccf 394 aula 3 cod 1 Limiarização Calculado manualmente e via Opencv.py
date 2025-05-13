import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
def histograma(imagem):
    histogram = cv.calcHist([imagem], [0], None, [256], [0, 256])
    # Plotar o histograma
    plt.figure(figsize=(10, 6))
    plt.title("Histograma de escala de cinza")
    plt.xlabel("Bins")
    plt.ylabel("# de Pixels")
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.show()
img = cv.imread('sudoku.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
histograma(img)
# find normalized_histogram, and its cumulative distribution function
hist = cv.calcHist([img],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.sum()
Q = hist_norm.cumsum()
plt.figure()
plt.title("Função de Densidade Acumulada")
plt.xlabel("pixels")
plt.plot(Q)
plt.xlim([0, 256])
plt.show()

bins = np.arange(256)
 
fn_min = np.inf
thresh = -1
 
for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
    q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
    if q1 < 1.e-6 or q2 < 1.e-6:
        continue
    b1,b2 = np.hsplit(bins,[i]) # weights
 
    # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
 
    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
 
# find otsu's threshold value with OpenCV function
ret, otsu = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print( "Threshold: calculado manualmente: {}  calculado pelo OpenCV: {}".format(thresh,ret) )
