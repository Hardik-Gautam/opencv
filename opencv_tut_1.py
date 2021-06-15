import cv2

# This is live video code
'''
cap = cv2.VideoCapture(0) # zero value is target default camera
while True:
    sucess, img = cap.read() # read function is returns images
    cv2.imshow('video', img) # this function is show the image which is captured by camera
    if cv2.waitKey(1) & 0xFF == ord('q'):break # this code stop the loop when user click the q buttion
'''


img = cv2.imread()
imgGray =