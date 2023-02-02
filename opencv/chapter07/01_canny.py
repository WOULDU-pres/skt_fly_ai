import numpy as np
import cv2


image = cv2.imread("images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")


def onMinThreshold(value):
    edge = cv2.Canny(image, value, 200) 
    cv2.imshow('Canny edge', edge)

def onMaxThreshold(value):
    edge = cv2.Canny(image, 0, value) 
    cv2.imshow('Canny edge', edge)
    
def cannyImg(image):
    cv2.namedWindow('Canny edge')
    cv2.createTrackbar('min', 'Canny edge', 0, 300, onMinThreshold)
    cv2.createTrackbar('max', 'Canny edge', 0, 300, onMaxThreshold)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cannyImg(image)

