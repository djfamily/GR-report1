import cv2
import numpy as np

img = cv2.imread('test.jpg',0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res = clahe.apply(img)
#cv2.imwrite('result.png', res)
cv2.imwrite('result.jpg', res)
cv2.imshow("Result", res)
