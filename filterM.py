
import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy
import math

def getRegion(u,v):
    global img
    global r
    global mask
    p = []
    for i in range(0,2*r+1):
        for j in range(0,2*r+1):
            if(mask[i,j]==1):
                p.append(img[u+i-r,v+j-r])
    return p
def AggDistance(x, P):
    d = 0
    for q in P:
        d = d +abs(x[0]-q[0])+abs(x[1]-q[1])+abs(x[2]-q[2])
    return d 
def fun2(x):
    global ind
    ind = x[0]
    s = list(map(fun,enumerate(x[1])))
    return s
def fun(x):
    u = ind
    v = x[0]
    pctr = x[1]
    P = getRegion(u,v)
    dctr = AggDistance(pctr,P)
    dmin = math.inf
    for pi in P:
        d = AggDistance(pi,P)
        if(d < dmin):
            pmin = pi
            dmin = d
    if (dmin < dctr):
        return pmin
    else:
        return x[1]
def Filter(img,r):
    m= img.shape[0]
    n =img.shape[1]
    img2 = copy.copy(img)
    centr = np.array(list(map(fun2,enumerate(img[r:m-r,r:n-r])))).reshape(m-2*r,n-2*r,3)
    img2[r:m-r,r:n-r] = centr
    return img2
            
            
img =cv2.imread("C:/Users/Acer/opencvProj/te.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img[0,0])
r = 3
mask = np.zeros((2*r+1,2*r+1),dtype=np.uint8)
for i in range(0,2*r+1):
    for j in range(0,2*r+1):
        if((i-r)**2+(j-r)**2)<=r*r:
            mask[i,j]=1
print(mask)
plt.imshow(img)
plt.show()
nimg = Filter(img,r)
cv2.imshow(nimg)
cv2.waitKey()

    