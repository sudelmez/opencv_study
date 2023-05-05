import cv2
import numpy as np 

img = cv2.imread("101/ders13/rain.jpg")
newfilter= cv2.blur(img,(3,3),)
medianfil= cv2.medianBlur(img,5)
gauss = cv2.GaussianBlur(img,(3,3),0)

cv2.imshow("filtered",newfilter)
cv2.imshow("not filtered",img)
cv2.imshow("median filtered",medianfil)
cv2.imshow("gauss filtered",gauss)


cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)
