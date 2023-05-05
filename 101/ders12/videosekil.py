import cv2
import numpy as np 

kamera = cv2.VideoCapture(1) 

while True: 
    ret, goruntu= kamera.read()

    cv2.rectangle(goruntu,(100,100),(200,200),(25,34,80),2)

    cv2.imshow("video kaydı", goruntu)

    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
kamera.release()    

cv2.destroyAllWindows()
