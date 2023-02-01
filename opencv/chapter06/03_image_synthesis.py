import numpy as np
import cv2
image1 = cv2.imread("../opencv/images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("../opencv/images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상파일 읽기 오류")


alpha, beta = 0.6,0.7



cv2.imshow("",image1)
cv2.waitKey(0)