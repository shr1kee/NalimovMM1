import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy
import math


class Filter:
    mask = []
    r = 1
    img = []
    k = 1

    def __init__(self, r, img, k):
        self.r = r
        self.img = img
        self.k = k

    def get_region(self, u, v):
        p = []
        for i in range(u - self.r, u + self.r + 1):
            for j in range(v - self.r, v + self.r + 1):
                p.append(self.img[i, j])
        return p

    def agg_distance(self, x, p):
        if self.k == 1:
            d = 0
            for q in p:
                d = d + abs(np.uint8(x[0] - q[0])) + abs(np.uint8(x[1] - q[1])) + abs(np.uint8(x[2] - q[2]))
            return d
        elif self.k == 2:
            d = 0
            for q in p:
                dq = math.sqrt((np.uint8(x[0] - q[0]))**2 + (np.uint8(x[1] - q[1]))**2 + (np.uint8(x[2] - q[2]))**2)
                d = d + dq
            return d
        else:
            d = 0
            for q in p:
                m = [abs(np.uint8(x[0] - q[0])), abs(np.uint8(x[1] - q[1])), abs(np.uint8(x[2] - q[2]))]
                dq = max(m)
                d = d+dq
            return d

    def fun(self, x):
        global p
        u = ind
        v = x[0]
        v = v + self.r
        pctr = x[1]
        dctr = self.agg_distance(pctr, p)
        dmin = math.inf
        for pi in p:
            d = self.agg_distance(pi, p)
            if (d < dmin):
                pmin = pi
                dmin = d
        for k in range(u - self.r, u + self.r + 1):
            p.append(self.img[k, v + 1])
        p = p[2*self.r+1:]
        if dmin < dctr:
            return pmin
        else:
            return pctr

    def fun2(self, x):
        global ind
        ind = x[0]
        ind = ind + self.r
        global p
        p = self.get_region(ind, self.r)
        s = list(map(self.fun, enumerate(x[1])))
        return s

    def vmf(self):
        m = self.img.shape[0]
        n = self.img.shape[1]
        img2 = copy.copy(self.img)
        centr = np.array(list(map(self.fun2, enumerate(self.img[self.r:m - self.r, self.r:n - self.r])))).reshape(
            m - 2 * self.r, n - 2 * self.r, 3)
        img2[self.r:m - self.r, self.r:n - self.r] = centr
        return img2
