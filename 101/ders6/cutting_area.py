import cv2
import numpy as np 

img = cv2.imread("101/ders6/wolf.jpg")

cv2.rectangle(img,(500,210),(150,150),[0,0,255],3)
cv2.imshow("new",img)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)
