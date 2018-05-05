import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy
import math


class Filter:
    mask = []
    r = 1
    img = []

    def __init__(self, r, img):
        self.r = r
        self.img = img
        self.mask = np.zeros((2 * r + 1, 2 * r + 1), dtype=np.uint8)
        for i in range(0, 2 * r + 1):
            for j in range(0, 2 * r + 1):
                if ((i - r) ** 2 + (j - r) ** 2) <= r * r:
                    self.mask[i, j] = 1

    def get_region(self, u, v):
        p = []
        for i in range(0, 2 * self.r + 1):
            for j in range(0, 2 * self.r + 1):
                if self.mask[i, j] == 1:
                    p.append(self.img[u + i - self.r, v + j - self.r])
        return p

    @staticmethod
    def agg_distance(x, p):
        d = 0
        for q in p:
            d = d + abs(np.uint8(x[0] - q[0])) + abs(np.uint8(x[1] - q[1])) + abs(np.uint8(x[2] - q[2]))
        return d

    def fun2(self, x):
        global ind
        ind = x[0]
        s = list(map(self.fun, enumerate(x[1])))
        return s

    def fun(self, x):
        u = ind
        v = x[0]
        pctr = x[1]
        P = self.get_region(u, v)
        dctr = self.agg_distance(pctr, P)
        dmin = math.inf
        for pi in P:
            d = self.agg_distance(pi, P)
            if (d < dmin):
                pmin = pi
                dmin = d
        if (dmin < dctr):
            return pmin
        else:
            return x[1]

    def VMF(self):
        m = self.img.shape[0]
        n = self.img.shape[1]
        img2 = copy.copy(self.img)
        centr = np.array(list(map(self.fun2, enumerate(self.img[self.r:m - self.r, self.r:n - self.r])))).reshape(
            m - 2 * self.r, n - 2 * self.r, 3)
        img2[self.r:m - self.r, self.r:n - self.r] = centr
        return img2
