import filterM
import cv2
import time
from matplotlib import pyplot as plt
img =cv2.imread("C:/Users/st/Desktop/Py/jesus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(50,50))
plt.subplot(221)
plt.imshow(img)
plt.subplot(222)
r = 2
t = time.clock()
nimg = filterM.Filter(r,img).Filter()
plt.imshow(nimg)
print(time.clock()-t)
plt.show()
