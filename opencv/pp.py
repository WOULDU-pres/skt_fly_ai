import numpy as np
import cv2 as cv

imgpath='./images/2.jpg'  # Image file path
sunglass = './images/shopping.png'
img = cv.imread(imgpath)   # Read image
sunglass = cv.imread(sunglass)
if img is None: raise Exception("Error reading image file")

face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# If a face is detected, get the coordinates
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Detect eyes in the face
    eyes = eye_cascade.detectMultiScale(gray[y:y+h, x:x+w])
    if len(eyes) >= 2:
        left_eye = eyes[0]
        right_eye = eyes[1]
        if left_eye[0] > right_eye[0]:
            left_eye, right_eye = right_eye, left_eye
        eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
        dy = right_eye[1] - left_eye[1]
        dx = right_eye[0] - left_eye[0]
        angle = np.degrees(np.arctan2(dy, dx))
        rotation_matrix = cv.getRotationMatrix2D(eye_center, angle, 1)
        resize_sunglass = cv.warpAffine(sunglass, rotation_matrix, (w, h))
    else:
        resize_sunglass = cv.resize(sunglass, (w, h))
        
    mask = cv.inRange(resize_sunglass, np.array([0, 0, 0]), np.array([0, 0, 0]))
    transparent_indices = np.where(mask == 0)
    roi = img[y:y+h, x:x+w]
    for channel in range(0, 3):
        roi[..., channel][transparent_indices] = resize_sunglass[..., channel][transparent_indices]


# Show the result with faces and eyes detected
cv.imshow('img',img)
cv.waitKey(0)

cv.destroyAllWindows()
