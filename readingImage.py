import cv2
import numpy as np

img = cv2.imread("image.jpg", -1)
#img = cv2.resize(img, (700,500))

#Create rectangle in image
img = cv2.rectangle(img, (300, 300), (200, 200), (134, 56, 132), 6)
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
print(img)
print(img.shape)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()