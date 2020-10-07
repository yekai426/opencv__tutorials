"""
The Canny edge detection algorithm is broken down to 5 steps:

Noise reduction;
Gradient calculation;
Non-maximum suppression;
Double threshold;
Edge Tracking by Hysteresis.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img, 100, 200)
#Canny edge detection. 100 is threshold 1, 200 is threshold 2

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()