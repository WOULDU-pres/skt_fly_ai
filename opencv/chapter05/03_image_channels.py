import cv2

image = cv2.imread('../images/photo.jpg', cv2.IMREAD_COLOR)
if image is None:
    raise Exception('영상 파일 읽기 오류')
if image.ndim != 3:
    raise Exception('컬러 영상 아님')

bgr = cv2.split(image)
print('bgr 자료형:', type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print('bgr 원소 개수:', len(bgr))

cv2.imshow('image', image)
cv2.imshow('blue channel:', bgr[0])
cv2.imshow('green channel:', bgr[1])
cv2.imshow('red channel', bgr[2])
cv2.waitKey(0)
