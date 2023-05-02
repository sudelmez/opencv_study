import cv2
import numpy as np 

wolf = cv2.imread("101/ders2/wolf.jpg")


print(wolf[(230,80)]) #renk olarak 222 blue,227 green, 230 red değeri geldi

# wolf[50,30]= [255,255,255] #belirtilen konumdaki piksel beyaz renge boyandı

for i in range(100):
    wolf[50,i]= [255,255,255] #belirtilen alan kadar beyaz boyar 



cv2.imshow("kurt",wolf)

cv2.waitKey(0) #pencere açıldığında pencerenin kalkması için tuşa basmamı bekler
cv2.destroyAllWindows() #çarpıya basınca opencv kapanır
cv2.waitKey(1)