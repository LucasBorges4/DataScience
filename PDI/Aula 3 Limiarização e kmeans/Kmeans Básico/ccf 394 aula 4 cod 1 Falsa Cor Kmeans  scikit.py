import numpy as np
import cv2
from sklearn.cluster import KMeans
img = cv2.imread('capacete.jpg')
'''
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

'''
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()

kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(Z)
# Now convert back into uint8, and make original image
center = np.uint8(kmeans.cluster_centers_)
res = center[kmeans.labels_]
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









































