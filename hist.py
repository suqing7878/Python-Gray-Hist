import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt


def imhist(img):
    cv.imshow("原始图像",img)
    channel_num = img.ndim
    if channel_num == 3:
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    cv.imshow('灰度图像', img)
    plt.title("灰度直方图")
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()



def equalhist(img):
    cv.imshow('原始图像',img)
    channel_num = img.ndim
    if channel_num == 3:
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imshow('灰度图像', img)
    plt.figure(1)
    plt.title('灰度直方图')
    plt.hist(img.ravel(), 256, [0, 256])
    img2=cv.equalizeHist(img)
    cv.imshow('灰度均衡化图像',img2)
    plt.figure(2)
    plt.title('灰度均衡化直方图')
    plt.hist(img2.ravel(), 256, [0, 256])

    plt.show()


