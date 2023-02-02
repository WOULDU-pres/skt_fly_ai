import cv2
def onTrackbar(th):
    rep_edge = cv2.GaussianBlur(rep_gray, (5,5), 0)
    rep_edge = cv2.Canny(rep_edge, th,th *2, 5)

    h, w = image.shape[:2]
    cv2.rectangle



image = cv2.imread("images/color_edge.jpg", cv2.IMREAD_COLOR)