import cv2
import matplotlib.pyplot as plt
import numpy as np

lower_green = np.array([0, 220, 0])     ##[R value, G value, B value]
upper_green = np.array([60, 255, 60])

videoV=cv2.VideoCapture("thanos.mp4")
videoP=cv2.VideoCapture("Praieiro.mp4")
contador=0
while True:
    ret,background_image = videoP.read()
    contador=contador+1
    if contador>200:
        ret,frameV=videoV.read()
        image_copy = np.copy(frameV)
        mask = cv2.inRange(image_copy, lower_green, upper_green)
        masked_image = np.copy(image_copy)
        masked_image[mask != 0] = [0, 0, 0]
        #cv2.imshow("saida2", masked_image)
        background_image=cv2.resize(background_image,(image_copy.shape[1],image_copy.shape[0]))
        crop_background =background_image[0:image_copy.shape[0], 0:image_copy.shape[1]]
        cv2.imshow("mascara", crop_background);
        cv2.waitKey(500)
        crop_background[mask == 0] = [0, 0, 0]
        cv2.imshow("mascara", crop_background);
        cv2.waitKey(500)
        background_image = crop_background + masked_image

    cv2.imshow("saida", background_image)
    cv2.waitKey(1)

    if cv2.waitKey(25)==27:
      break
video.release()
#video2.release()
cv2.destroyAllWindows()
  


    

'''
    

        
'''
    
