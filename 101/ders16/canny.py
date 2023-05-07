import cv2
import numpy as np 

image= cv2.imread("101/ders16/grogu.webp",0) #gri olmalı, sonra blurlama yapılmalı(istemedğimiz küçük kenarları yok etmek için,yumuşatmak)
blur = cv2.GaussianBlur(image,(3,3),0)
canny1= cv2.Canny(blur,30,150) #alt üst eşik değerli

def otoCanny(blur, sigma=0.33):
    medyan=np.median(blur) #piksel yoğunlukların medyanını hesapladık
    lower = int(max(0,((1.0)-sigma)*medyan)) #otomatize ettiğimiz yer. sigmaya göre. alt eşik değeri
    upper = int(min(0,((1.0)+sigma)*medyan)) #üst eşik değeri
    canny2=cv2.Canny(blur,lower,upper)
    
    return canny2

# cv2.imshow("grogu",blur)
# cv2.imshow("grogu canny",canny1 )
# cv2.imshow("grogu canny with def",otoCanny(blur) )

cv2.imshow("edges",np.hstack([blur,canny1,otoCanny(blur)]))

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)