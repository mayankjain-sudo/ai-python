import cv2

img = cv2.imread("image.jpg", -1)
img = cv2.rectangle(img, (300, 300), (200, 200), (134, 56, 132), 6)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()