import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# haarcascade_frontalface_default.xml you can download it from open cv github
# https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

img = cv2.imread('people.jpg')
# replace people.jpg with any image that contain faces to test it out

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

cv2.imshow('img', img)

cv2.waitKey()

cv2.imwrite("face_detected.jpg")
