import numpy as np
import cv2

def detectFace(frame):
    # Classifiers that are going to be passed through pixels
    faceCascade=cv2.CascadeClassifier('haarcascade_classifiers/haarcascade_frontalface_default.xml')
    leftEyeCascade=cv2.CascadeClassifier('haarcascade_classifiers/haarcascade_lefteye_2splits.xml')
    rightEyeCascade=cv2.CascadeClassifier('haarcascade_classifiers/haarcascade_righteye_2splits.xml')
    faceRect=faceCascade.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=5) # returns (x,y) and (w,h) coordinates

    for(x,y,w,h) in faceRect:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=2) # Drawing rectangle around ROI
        
        leftEyeRect=leftEyeCascade.detectMultiScale(frame,scaleFactor=3,minNeighbors=6)
        rightEyeRect=rightEyeCascade.detectMultiScale(frame,scaleFactor=3,minNeighbors=6)
    
        for(x,y,w,h) in leftEyeRect: 
            cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=2) 
            
        for(x,y,w,h) in rightEyeRect: 
            cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=1)
        
    return frame


cap=cv2.VideoCapture(0) # Captures default laptop or computer camera

if cap.isOpened()==False:
    print("Error wrong codec or cam is in use")

while cap.isOpened()==True:
    ret,frame=cap.read() # Grabs the frames continuously
    frame=detectFace(frame)
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(10) & 0xFF==27: # Press esc to exit
        break
    
cap.release()
cv2.destroyAllWindows()