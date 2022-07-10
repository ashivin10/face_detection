#FACE RECoginition
import cv2
vid_src="face.mp4"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(vid_src)

while True:
    ret,frame = cap.read();
    if(type(frame)==type(None)):
        break
    

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor = 2.4,minNeighbors =8)


    for x,y,w,h in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)

    cv2.imshow('FACE RECOGNITION',img)
    if ( cv2.waitKey(1)==13):
         break
cv2.destroyAllWindows()
    
