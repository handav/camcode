import cv2
import numpy as np

img = cv2.imread("insta_pics/2.jpg")
BLUE_MIN = np.array([100, 0, 0], np.uint8)
BLUE_MAX = np.array([255, 50, 50], np.uint8)

dst = cv2.inRange(img, BLUE_MIN, BLUE_MAX)
cv2.imshow('dst', dst)
cv2.waitKey(0)
no_blue = cv2.countNonZero(dst)
print('The number of blue pixels is: ' + str(no_blue))
cv2.namedWindow("opencv")
cv2.imshow("opencv",img)
cv2.waitKey(0)