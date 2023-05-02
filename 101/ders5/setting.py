import cv2
import numpy as np 

img = cv2.imread("101/ders5/aiexample.webp")

newimg =cv2.copyMakeBorder(img,80,80,470,470,cv2.BORDER_REFLECT)#aynalama
newimg2= cv2.copyMakeBorder(img,200,200,200,200,cv2.BORDER_REPLICATE)#uzatma
newimg3= cv2.copyMakeBorder(img,200,200,200,200,cv2.BORDER_WRAP)#tekrar
newimg4= cv2.copyMakeBorder(img,200,200,200,200,cv2.BORDER_CONSTANT,value=(75,160,200))#sarılan

cv2.imshow("yansımış fotoğraf",newimg)
cv2.imshow("uzamış fotoğraf",newimg2)
cv2.imshow("uzamış fotoğraf",newimg3)
cv2.imshow("uzamış fotoğraf",newimg4)


cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)