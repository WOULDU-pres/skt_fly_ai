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
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)


    
    # Calculate the angle of rotation for the sunglasses
    if len(eyes) == 2:
        eye1 = eyes[0]
        eye2 = eyes[1]
        if eye1[0] > eye2[0]:
            eye1, eye2 = eye2, eye1

        x1, y1 = eye1[0], eye1[1]
        x2, y2 = eye2[0], eye2[1]
        dx = x2 - x1
        dy = y2 - y1
        angle = np.degrees(-np.arctan2(dy, dx))

        # Resize the sunglasses
        resize_sunglass = cv.resize(sunglass, (w, h))

        # Rotate the sunglasses
        rows, cols = resize_sunglass.shape[:2]
        rot_mat = cv.getRotationMatrix2D((cols/2, rows/2), angle, 1)
        result = cv.warpAffine(resize_sunglass, rot_mat, (cols, rows), flags=cv.INTER_LINEAR)

        # Create the mask for transparent pixels in the sunglasses
        mask = cv.inRange(result, np.array([0, 0, 0]), np.array([0, 0, 0]))
        transparent_indices = np.where(mask == 0)

        # Overlay the sunglasses on the face
        roi = img[y:y+h, x:x+w]
        for channel in range(0, 3):
            roi[..., channel][transparent_indices] = result[..., channel][transparent_indices]

# Show the result with faces and eyes detected
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
