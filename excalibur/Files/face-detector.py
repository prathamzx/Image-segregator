import cv2
#import os

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("test2.jpg")


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.2,
minNeighbors=5)



for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)


resized=cv2.resize(img,(int(img.shape[1]/6),int(img.shape[0]/6)))


cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
