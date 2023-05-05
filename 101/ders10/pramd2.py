import cv2
import numpy as np 

kamera = cv2.VideoCapture(1) #0 dersem pcdeki kamerayı alır, 1 usb ile takılı olan, 2  tanımlanmış bi videodan alır

while True: #ret, kamera çalışma kontrolü
    ret, goruntu= kamera.read()
    cv2.imshow("video kaydı", goruntu)

    #30ms de bir görüntü çek
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
kamera.release()    

cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)




