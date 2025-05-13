'''
Finds lines in a binary image using the standard Hough transform.

The function implements the standard or standard multi-scale Hough transform algorithm for line detection.
See http://homepages.inf.ed.ac.uk/rbf/HIPR2/hough.htm for a good explanation of Hough transform.

Parameters
    image	8-bit, single-channel binary source image. The image may be modified by the function.
    lines	Output vector of lines. Each line is represented by a two-element vector (ρ,θ) .
                ρ is the distance from the coordinate origin (0,0) (top-left corner of the image).
                θ is the line rotation angle in radians ( 0∼vertical line,π/2∼horizontal line ).
    rho	        Distance resolution of the accumulator in pixels.
    theta	Angle resolution of the accumulator in radians.
    threshold	Accumulator threshold parameter. Only those lines are returned that get enough votes ( >threshold ).
    srn	        For the multi-scale Hough transform, it is a divisor for the distance resolution rho .
                The coarse accumulator distance resolution is rho and the accurate accumulator resolution is rho/srn .
                If both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these parameters should be positive.
    stn	        For the multi-scale Hough transform, it is a divisor for the distance resolution theta.
    min_theta	For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 0 and max_theta.
    max_theta	For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between min_theta and CV_PI.
    '''
print(__doc__)



# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Reading the required image in 
# which operations are to be done. 
# Make sure that the image is in the same 
# directory in which this python program is
img = cv2.imread('campus1.png')
l,c,cor=img.shape
cl=int(l/2)
cc=int(c/2)
print(cc,cl)
img=img[int(cl/2):int(3*cl/2),int(cc/2):int(3*cc/2)]
 
# Convert the img to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# Apply edge detection method on the image
edges = cv2.Canny(gray,50,150,apertureSize = 3)
#cv2.imshow('Saida com bordas',edges)

 
# This returns an array of r and theta values
'''
First parameter, Input image should be a binary image,
  so apply threshold edge detection before finding applying hough transform.
Second and third parameters are r and θ(theta) accuracies respectively.
Fourth argument is the threshold, which means minimum vote it should get for it to be considered as a line.
Remember, number of votes depend upon number of points on the line.
 So it represents the minimum length of line that should be detected.
'''
lines = cv2.HoughLines(edges,1,np.pi/180,100)
print(len(lines))
 
# The below for loop runs till r and theta values 
# are in the range of the 2d array
for i in range(len(lines)):
 for rho,theta in lines[i]:
#    print('%d' % rho, '%d' % theta)
     
    # Stores the value of cos(theta) in a
    a = np.cos(theta)
 
    # Stores the value of sin(theta) in b
    b = np.sin(theta)
     
    # x0 stores the value rcos(theta)
    x0 = a*rho
     
    # y0 stores the value rsin(theta)
    y0 = b*rho
     
    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 1000*(-b))
     
    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 1000*(a))
 
    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 1000*(-b))
     
    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 1000*(a))
     
    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0,0,255) denotes the colour of the line to be 
    #drawn. In this case, it is red. 
    cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
     
# All the changes made in the input image are finally
# written on a new image houghlines.jpg

cv2.imshow('saida',img)
cv2.imwrite('LinhasDetectadas.jpg',img)
