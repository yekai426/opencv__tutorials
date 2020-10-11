"""
Template Matching is a method for searching and finding the location of a template image in a larger image.
"""
import cv2
import numpy as np

img = cv2.imread("messi5.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg", 0)
w, h = template.shape[::-1]
# shape return row and column. [::-1] is to reverse row, column order to column and row

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED)
print(res)
threshold = 0.99
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
# * is to create tuple, [::-1] is to reverse row, column order to column and row
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()