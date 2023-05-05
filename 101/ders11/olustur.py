import cv2
import numpy as np 

resim = np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(0,0,255),3) #0,0dan başlayıp 100,100e gidecek çizgi. son parametre bgr ve kalınlık

cv2.circle(resim,(150,150),20,(255,0,0),2)

cv2.putText(resim,"deneme texti",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,30,90))

cv2.imshow("deneme",resim)



cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)

