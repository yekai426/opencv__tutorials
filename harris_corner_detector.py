"""
Detect corners with Harris Corner Detector
"""

import numpy as np
import cv2 as cv

img = cv.imread('chessboard.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
# mark corner as red color, corner signal is (dst > 0.01 * dst.max())

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
