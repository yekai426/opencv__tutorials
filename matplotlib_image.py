import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', -1)
#opencv read image in BGR format
cv2.imshow('image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
#matplotlib read image in RGB format
plt.xticks([]), plt.yticks([])
# hide x and y coordinates
plt.show()

