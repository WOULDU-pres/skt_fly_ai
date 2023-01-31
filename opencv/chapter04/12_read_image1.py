import cv2
from common.utils import print_mat_info

title1, title2 = 'gray2gray', 'gray2color'
gray2gray = cv2.imread('../images/gray.png', cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread('../images/gray.png', cv2.IMREAD_COLOR)

if gray2gray is None or gray2color is None:
    raise Exception('영상 파일 읽기 에러')

print('행렬 좌표 (100, 100) 최소값')
print('%s %s' % (title1, gray2gray[100, 100]))
print('%s %s' % (title2, gray2color[100, 100]))

print_mat_info(title1, gray2gray)
print_mat_info(title2, gray2color)

cv2.imshow(title1, gray2gray)
cv2.imshow(title2, gray2color)
cv2.waitKey(0)
