"""
How to use opencv Histograms function.
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg", 0)
# read grayscale image
#img = np.zeros((200,200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)


hist = cv.calcHist([img], [0], None, [256], [0, 256])
# [0] is 0 channel
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()