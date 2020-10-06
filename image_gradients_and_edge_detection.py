"""
How to use Image Gradients and Edge Detection with OpenCV.
OpenCV provides three types of gradient methods or High-pass filters, Sobel, Scharr and Laplacian.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
# convert from float to integer
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# 1 is dx and x direction, 0 is dy and y direction. sobelX is change intensity in y direction
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
# 0 is dx and x direction, 1 is dy and y direction. sobelY is change intensity in x direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()