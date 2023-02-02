import numpy as np
import cv2

image1 = cv2.imread("../opencv/images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("../opencv/images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상파일 읽기 오류")

def onChange(x):
    pass
    
def imgAddWeighted(image1, image2):
    cv2.namedWindow('Img')
    cv2.createTrackbar('beta', 'Img', 0, 10, onChange)
    cv2.createTrackbar('alpha', 'Img', 0, 10, onChange)

    cv2.setTrackbarPos("alpha", "Img", 9)
    cv2.setTrackbarPos("beta", "Img", 2)
    
    while True:
        alpha = cv2.getTrackbarPos('alpha', 'Img')
        beta = cv2.getTrackbarPos('beta', 'Img')
        img = cv2.addWeighted(image1, float(alpha)* 0.1, image2, float(beta) * 0.1, 0)
        cv2.imshow('Img', img)
        
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

imgAddWeighted(image1,image2)