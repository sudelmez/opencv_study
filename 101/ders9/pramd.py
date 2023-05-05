import cv2
import numpy as np 

resim = cv2.imread("101/ders9/wolf.jpg")

ikikat= cv2.pyrUp(resim) #görsel iki kat büyür
ikikatkucuk= cv2.pyrDown(resim) #görsel iki kat küçülür

# cv2.imshow("bir",resim)
# cv2.imshow("iki",ikikat)
# cv2.imshow("uc",ikikatkucuk)
# print(resim.shape)
# print(ikikatkucuk.shape)

#numpy matris oluşturuyor
#300 yükseklik, genişlik ve 3 kanaldan oluşan bir shape verdik. ikinci parametre datatype.
foto = np.zeros((300,300,3),dtype="uint8") #matris oluşturuyor

print(foto)



cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)




