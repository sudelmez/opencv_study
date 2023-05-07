import cv2
import numpy as np 

img = cv2.imread("101/ders14/rain.jpg")

kernel = np.zeros((5,5),np.uint8)

opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #sırasıyla erosion ve dilation işlemleri sonrası görsel daha temşz hale geliyor. bu fonksiyon bu amacı gerçekleştiriyor.
closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel) #opening in tam tersi
gradyan = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) #erosion ve dilation arasındaki farkı gösterir..dilation-erosion
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel) #orijinal-opening farkını gösterir. arka plandaki görselleri gösterir
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel) #orijinal-closing farkını gösterir. arka plandaki görselleri gösterir


cv2.imshow("orjinl", img)
cv2.imshow("opening", opening )
cv2.imshow("gradyan", gradyan )
cv2.imshow("tophat", tophat )
cv2.imshow("blackhat", blackhat )


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
