import cv2
import numpy as np 

#burada gruplandırm, bölgeye göre eşik değeri ayarlanabiliyor
image= cv2.imread("101/ders15/color.jpg",0) #gri tonlamalı olmalı


ret,thresh = cv2.threshold(image,160,255,cv2.THRESH_BINARY) #simple thresholding

thresh2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,23,2) #piksel sınırları
t#karmaşık görsellerde belirli bir bölge için istediğimiz gibi thresh uygulaması yaparız.
thresh3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,23,2) 
 
cv2.imshow("thresh",thresh)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
