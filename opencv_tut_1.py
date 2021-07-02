import numpy as np
import cv2

# This is live video code
r'''
cap = cv2.VideoCapture(0) # zero value is target default camera
while True:
    sucess, img = cap.read() # read function is returns images
    cv2.imshow('video', img) # this function is show the image which is captured by camera
    if cv2.waitKey(1) & 0xFF == ord('q'):break # this code stop the loop when user click the q buttion
'''

# This is show for an image
r'''img = cv2.imread(r'C:\Users\Hardik Gautam\Desktop\Python Programs\My website\Images\9.jpg')
cv2.imshow('wallpaper',img)
cv2.waitKey(0)
'''

# This is image color section 
r'''
cap = cv2.VideoCapture(0)

kernel = np.ones((5,5),np.uint8)
print(kernel)

while True:
    success, im = cap.read()
    imggray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # Thsi is set color of an image
    imgblure = cv2.GaussianBlur(imggray,(9,9),0) # parameter(image_var,(bluernesss),bluer_power)
    imgcanny = cv2.Canny(im,110,110 )# this make an black and white line iamge its parameter is image_var and black and white color value
    imgblure2 = cv2.GaussianBlur(imggray,(9,9),500) # parameter(image_var,(bluernesss),bluer_power)
    imgdialation = cv2.dilate(imgcanny,kernel,iterations=1) # this is make an black white linek image and itrations para.. is thickness of white lines
    imEroded = cv2.erode(imgdialation,kernel,iterations=1)

    # cv2.imshow("Gray image",imggray)
    # cv2.imshow('gaussion bulre',imgblure)
    # cv2.imshow('gaussion buler 2',imgblure2)
    # # cv2.imshow('Canny Image',imgcanny)
    # cv2.imshow('image is dialation',imgdialation)
    # cv2.imshow('Eroded Image',imEroded)


    if cv2.waitKey(1) & 0XFF == ord('q'):break

'''

r'''
# This is image Resizing and Cropping section
# Resizing image
img = cv2.imread(r'D:\45.jpg')
print(img.shape)
# imgresize = cv2.resize(img,(500,300))
# cv2.imshow('image',img)
# cv2.imshow('image resize',imgresize)
# print(imgresize.shape)

# this is crop method of an image its take wdith and height
cv2.imshow('image',img)
imgcropped =  img[0:600,600:1000]
cv2.imshow('Crop Image',imgcropped)
cv2.waitKey(0)
'''

# Shape and text write
r'''
img =  cv2.imread(r'D:\45.jpg')
# print(img.shape)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),color=(0,255,0),thickness=1)
cv2.rectangle(img,(0,0),(250,350),color=(0,0,255),thickness=2)
cv2.circle(img,(400,100),100,color=(255,255,0),thickness=2)
cv2.putText(img,"This image is create by me",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),thickness=3)
cv2.imshow('image',img)
cv2.waitKey(0)
'''

# Warp prespective

img =  cv2.imread(r'D:\45.jpg')
height, width = 1080, 1920

s1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
s2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrixx = cv2.getPerspectiveTransform(s1,s2)
imageoutput = cv2.warpPerspective(img,matrixx,(width,height))
cv2.imshow('image',imageoutput)
cv2.waitKey(0)
