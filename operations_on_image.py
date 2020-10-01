import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)
# return a tuple of rows, columns, and channels

print(img.size)
# return total number of pixels

print(img.dtype)
# return image data type

b, g, r = cv2.split(img)
# split image into BGR channels

img = cv2.merge((b, g, r))

ball = img[280: 340, 330: 390]
img[273:333, 100:160] = ball
cv2.imshow('image', img)

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# before add two image, two image must be the same size

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
cv2.imshow('AddImage', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()