import cv2
import numpy as np 

# image = cv2.imread("aiexample.webp")
image = cv2.imread("101/ders1/aiexample.webp",0) #fotoğrafı gri okur, kanalı 0 okudu

cv2.imshow("ai logo", image)

cv2.imwrite("101/ders1/blackai.webp",image) #yeni fotoğraf oluşturdu

print(image) #görselin piksel ölçülerini matris şeklinde verir
print(image.size) 
print(image.dtype) 
print(image.shape) 

cv2.waitKey(0) #pencere açıldığında pencerenin kalkması için tuşa basmamı bekler
cv2.destroyAllWindows() #çarpıya basınca opencv kapanır
cv2.waitKey(1)