import numpy as np
import cv2 as cv

imgpath='./images/2.jpg'  # Image file path
sunglass = './images/shopping.png'
img = cv.imread(imgpath)   # Read image
sunglass = cv.imread(sunglass)
if img is None: raise Exception("Error reading image file")


face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# If a face is detected, get the coordinates
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    resize_sunglass = cv.resize(sunglass, (w, h))
    roi_color = img[y:y+h, x:x+w]
    
    # Put sunglass on the face
    roi_color = resize_sunglass
        
# Show the result with faces and eyes detected
cv.imshow('img',img)
cv.waitKey(0)

cv.destroyAllWindows()
