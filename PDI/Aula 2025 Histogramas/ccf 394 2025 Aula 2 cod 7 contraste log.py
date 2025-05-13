import cv2
import numpy as np
import matplotlib.pyplot as plt
   
# Read an image
image = cv2.imread('wiki.png', cv2.IMREAD_GRAYSCALE)
   
# Apply log transformation method
c = 255 / np.log(1+np.max(image))
print(np.max(image))
print(c)
log_image = c * (np.log(image + 1))
print(log_image)
   
# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)
   
# Display both images
cv2.imshow("Entrada", image)

cv2.imshow("saida", log_image)
cv2.waitKey(0)
