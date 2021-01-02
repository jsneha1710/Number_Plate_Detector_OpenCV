import cv2
import numpy as np
# cap=cv2.VideoCapture(0)  #to capture video from webcam (0) and from file(1)
# cap.set(3,640) #setting the width and height
# cap.set(4,480)
# cap.set(10,150)
# while True:
#     success,img=cap.read()
img = cv2.imread(r"C:\Users\Sneha\Pictures\car2.png")
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
nplateCascade = cv2.CascadeClassifier(r"C:\Users\Sneha\Documents\haarcascade_russian_plate_number.xml")
plates = nplateCascade.detectMultiScale(imggray, 1.1, 4)

for (x, y, w, h) in plates:
    area=w*h
    if(area>50):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        imgroi=img[y:y+h,x:x+w]
        cv2.imshow("Cropped",imgroi)
cv2.imshow("Image",img)
cv2.waitKey(0)

#if cv2.waitKey(1) & 0xFF==ord('q'):
    #break