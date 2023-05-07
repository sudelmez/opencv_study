import cv2
import numpy as np 

image= cv2.imread("101/ders17/blackwhite.jpg") 
image2= cv2.imread("101/ders17/image.png") 

image = image[0:350,0:350]
image2 = image2[0:350,0:350]

bit_and = cv2.bitwise_and(image,image2) #siyah 0, beyaz 1 gibi düşünüyor
bit_or = cv2.bitwise_or(image,image2) #siyah 0, beyaz 1 gibi düşünüyor
bit_xor = cv2.bitwise_xor(image,image2) #siyah 0, beyaz 1 gibi düşünüyor

cv2.imshow("and",bit_and)
cv2.imshow("or",bit_or)
cv2.imshow("xor",bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)