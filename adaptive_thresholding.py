import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# cv.ADAPTIVE_THRESH_MEAN_C is adaptive method, cv.THRESH_BINARY is threshold type, 11 is block size, 2 is C value
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# cv.ADAPTIVE_THRESH_GAUSSIAN_C is adaptive method, cv.THRESH_BINARY is threshold type, 11 is block size, 2 is C value

cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.waitKey(0)
cv.destroyAllWindows()