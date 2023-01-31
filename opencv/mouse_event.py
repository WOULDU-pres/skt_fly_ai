"""
PC 카메라를 통해 받아온 프레임에 다음의 영상처리를 수행하고, 결과 영상을 
윈도우에 표시하는 프로그램을 작성하시오
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frame_rate = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)

while True:
    ret, frame = cap.read()
    if not ret or cv2.waitKey(delay) >= 0: break
    blue, green, red = cv2.split(frame)


    frame[100:300, 200:300] += np.array([0, 50, 0], np.uint8)
    cv2.rectangle(frame, 0, 0, (0, 0, 255), 3)
    frame = cv2.merge([blue, green, red])
    cv2.imshow("qwe", frame)

cap.release()



# import cv2
# import numpy as np


# capture = cv2.VideoCapture(0)
# if not capture.isOpened(): raise Exception('안열려요')

# frame_rate = capture.get(cv2.CAP_PROP_FPS)
# delay = int(1000/frame_rate)
# pt1,pt2 = (200,100),(300,300)

# while True:
#     ret,frame = capture.read()
#     if not ret or cv2.waitKey(delay) >= 0: break    # 프레임 간 지연 시간 지정
#     blue,green,red = cv2.split(frame)
#     cv2.add(green[100:300,200:300],50,green[100:300,200:300])
#     frame = cv2.merge([blue,green,red])
#     cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
#     cv2.imshow('my video',frame)
# capture.relase()