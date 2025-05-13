import cv2 
 
cap = cv2.VideoCapture(0)
cont=0
# Check if the webcam is opened correctly 
if not cap.isOpened(): 
    raise IOError("Cannot open webcam") 
 
while True: 
    ret, frame = cap.read()
    if ret == True:
      frame = cv2.resize(frame, None, fx=0.9, fy=0.9, interpolation=cv2.INTER_AREA)
      frame = cv2.flip(frame,1)
      cv2.imshow('Input', frame) 
 
      c = cv2.waitKey(1)
      # cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(cont)), frame)  
      #      cont += 1
      if c == 27: 
        break 
 
cap.release() 
cv2.destroyAllWindows() 


