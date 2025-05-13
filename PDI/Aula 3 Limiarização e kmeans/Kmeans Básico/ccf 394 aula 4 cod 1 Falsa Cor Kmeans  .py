import numpy as np
import cv2
img = cv2.imread('capacete.jpg')
'''
Input parameters
samples : It should be of np.float32 data type, and each feature should be put in a single column.

nclusters(K) : Number of clusters required at end

criteria : It is the iteration termination criteria. When this criteria is satisfied, algorithm iteration stops.
Actually, it should be a tuple of 3 parameters. They are `( type, max_iter, epsilon )`:
type of termination criteria. It has 3 flags as below:
  cv.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached.
  cv.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter.
  cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.
  
max_iter - An integer specifying maximum number of iterations.

epsilon - Required accuracy

attempts : Flag to specify the number of times the algorithm is executed using different initial labellings.
The algorithm returns the labels that yield the best compactness. This compactness is returned as output.

flags : This flag is used to specify how initial centers are taken. Normally two flags are used for this : cv.KMEANS_PP_CENTERS and cv.KMEANS_RANDOM_CENTERS.

Output parameters
  compactness : It is the sum of squared distance from each point to their corresponding centers.
  labels : This is the label array (same as 'code' in previous article) where each element marked '0', '1'.....
  centers : This is array of centers of clusters.


'''
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
final=np.concatenate((img,res2),axis=1)
cv2.imshow('res2',final)

print("Centro do cluster 0:",center[0])
print("Centro do cluster 1:",center[1])
print("Centro do cluster 2:",center[2])

k1 = np.ones((100,100,3),np.uint8)
k2=np.ones((100,100,3),np.uint8)
k3=np.ones((100,100,3),np.uint8)
k1[:,:,0]=[center[0][0]]
k1[:,:,1]=[center[0][1]]
k1[:,:,2]=[center[0][2]]

k2[:,:,0]=[center[1][0]]
k2[:,:,1]=[center[1][1]]
k2[:,:,2]=[center[1][2]]

k3[:,:,0]=[center[2][0]]
k3[:,:,1]=[center[2][1]]
k3[:,:,2]=[center[2][2]]

final=np.concatenate((k1,k2,k3),axis=1)

cv2.imshow("cores dos clusters",final)
cv2.waitKey(0)
cv2.destroyAllWindows()









































