import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt
import hist


img=cv.imread('1.jpg')
cv.imshow('原始图像',img)
img2=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
hist.equalhist(img2)
cv.waitKey(0)