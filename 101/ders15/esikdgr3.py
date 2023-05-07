import cv2
import numpy as np 

image= cv2.imread("101/ders15/color.jpg",0)
#burası değer seçme zorunluluğunu kaldırır, kendi belirler... otsu yöntemi! orijinale çok daha yakın sonuç verir

ret,thresh = cv2.threshold(image,160,255,cv2.THRESH_BINARY) #simple thresholding
ret2,thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU) #otsu thresholding..eşik değer için min ve maks verdik. eşik değerini kendi belirleyecek



cv2.imshow("thresh",thresh)
cv2.imshow("thresh2",thresh2)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
