import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)
# kernel is 5 by 5 square with white color

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# opening is applying erosion first and then dilation on image
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# closing is applying dilation first and then erosion on image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
# morph gradient is difference between dilation and erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
# tophat is difference between image and opening

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()