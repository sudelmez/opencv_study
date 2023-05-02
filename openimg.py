import cv2
import numpy as np 

# image = cv2.imread("aiexample.webp")
image = cv2.imread("aiexample.webp",0) #fotoğrafı gri okur

cv2.imshow("ai logo", image)

cv2.imwrite("blackai.webp",image) #yeni fotoğraf oluşturdu

cv2.waitKey(0) #pencere açıldığında pencerenin kalkması için tuşa basmamı bekler
cv2.destroyAllWindows() #çarpıya basınca opencv kapanır
cv2.waitKey(1)