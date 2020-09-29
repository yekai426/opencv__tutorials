import cv2

img = cv2.imread('lena.jpg', -1)
# 1 is to load color image, 0 is to load grayscale image, -1 is to load unchanged image
cv2.imshow('image', img)
# 'image' is window name
k = cv2.waitKey(0) & 0xFF
# 0 mill seconds, infinite wait
# 0xFF is mask used for 64 bits OS

if k == 27:
  # 27 is escape key
  cv2.destroyAllWindows()
elif k == ord('s'):
  # s is s key
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()
