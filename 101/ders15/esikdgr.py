import cv2
import numpy as np 

#burada tek tip eşik değeri ile işlem yapılıyor

image= cv2.imread("101/ders15/color.jpg")

ret, thresh1= cv2.threshold(image,127,255,cv2.THRESH_BINARY)#127 eşik değeri. piksel değeri 127nin altında olanlar 0a yuvarlansın! 255 ise maks değer.127nin üstündeyse 255e çıkar
ret, thresh2= cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3= cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret, thresh4= cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret, thresh5= cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("orijinal",image)
cv2.imshow("thresh",thresh1 )
cv2.imshow("thresh2",thresh2 )
cv2.imshow("thresh3",thresh3 )
cv2.imshow("thresh4",thresh4 )
cv2.imshow("thresh5",thresh5 )

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
