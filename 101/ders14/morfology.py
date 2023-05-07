import cv2
import numpy as np 

img = cv2.imread("101/ders14/rain.jpg")

kernel = np.zeros((5,5),np.uint8)

dilation = cv2.dilate(img,kernel,iterations=1) #beyaz bölge artıyor, gürültüler artıyor.genişleme işlemi yapıyor
erosion = cv2.erode(img,kernel,iterations=1)  #dilationun tam tersi

cv2.imshow("dilation", dilation)
cv2.imshow("erosion", erosion)
cv2.imshow("orjinl", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
