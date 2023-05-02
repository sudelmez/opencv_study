import cv2
import numpy as np 

desen = cv2.imread("101/ders4/desen.jpg")

part= desen[200:300,300:400]

cv2.imshow("kesit alanı",part)
cv2.imshow("tam",desen)

desen[0:100,0:100]=part
cv2.imshow("tam",desen)


cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)