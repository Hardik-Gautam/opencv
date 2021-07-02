import cv2
from numpy.core.fromnumeric import resize
from numpy.lib.function_base import _calculate_shapes

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('beauty.jpg')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x, y, w, h in face:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
resized = cv2.resize(img,(700,500))

cv2.imshow('gray',resized) 
cv2.waitKey(0) 