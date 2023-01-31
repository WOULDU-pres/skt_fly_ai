import numpy as np
import cv2


def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print('추가 화소값:', add_value)
    image += np.uint8(add_value)
    cv2.imshow(title, image)


def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if 246 <= image[0][0] <= 255:
            image.fill(255)
        elif image[0][0] < 246:
            image += np.uint8(10)
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        if image[0][0] < 10:
            image.fill(0)
        elif image[0][0] >= 10:
            image -= np.uint8(10)
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)

title = 'Trackbar Event & Mouse Event'
bar_name = 'Brightness'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
