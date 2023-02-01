import numpy as np, cv2

image = cv2.imread("chap05/images/sum_test.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")
    
mask = np.zeros(image.shape[:2], np.uint8)
mask[60:160, 20:120] = 255                      # 관심영역을 지정한 후, 255를 할당

sum_value   = cv2.sumElems(image)               # 채널별 합 구하기
mean_value1 = cv2.mean(image)                   # 결과 튜플로 반환
mean_value2 = cv2.mean(image, mask)

print('sum_value 자료형:', type(sum_value), type(sum_value[0]))
print("[sum_value] = ", sum_value)
print("[mean_value1] = ", mean_value1)
print("[mean_value2] = ", mean_value2)
print()