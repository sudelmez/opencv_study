import cv2
import numpy as np 

foto=cv2.imread("101/ders8/yesil.jpg")
# foto=cv2.imread("101/ders8/yesil.jpg",0) böyle de grileşir

greyfoto= cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY) #grileştirdi. kanal 1e düştü

yukseklik, genislik, kanalSayisi = foto.shape #gerekli yerleri soldaki değerlere attı
yukseklikgr, genislikgr = greyfoto.shape #gerekli yerleri soldaki değerlere attı

print(yukseklik ," " ,genislik ," " ,kanalSayisi)
print(yukseklikgr ," " ,genislikgr )

cv2.imshow("gri",greyfoto)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)
