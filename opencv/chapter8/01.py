import numpy as np
import cv2

image = cv2.imread("images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 찾기 에러")

size = (350, 400)
dst3 = cv2.resize(image, size, cv2.INTER_LINEAR)
dst4 = cv2.resize(image, size, cv2.INTER_NEAREST)

cv2.imshow("image", image)
cv2.imshow("OpenCV_bilinear", dst3)
cv2.imshow("OpenCV_Nearest", dst4)
cv2.waitKey(0)