import cv2
import numpy as np

x = np.array([[1,2],[3,4]],np.uint8)
y = np.array([[-10,11],[12,-34]])
msk = int(y > 0)
print(msk)
z = np.zeros((2,2,2))
z[:, :,0] = x
z[:, :, 1] = y
print(z[0,0])
# z = np.ones((2,2,2))
# for i in range(0,2):
#     for j in range(0,2):
#         z[i,j] = [x[i,j],y[i,j]]
# print(type (z[0,0,0]))