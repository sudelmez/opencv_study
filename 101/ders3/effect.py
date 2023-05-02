import cv2
import numpy as np 

desen = cv2.imread("101/ders3/desen.jpg")


# desen[:,:,0]=255 #bgr kısmıyla oynadık, blue kısmıyla oynayıp tam blue yaptık
# desen[:,:,1]=100 #burada green kısmıyla oynadık
# # desen[:,:,2]=200 #burada red kısmıyla oynadık

desen[300:500,700:800,0]=255
desen[300:500,700:800,1]=100 #burada belirli alanların efektini uygular

cv2.imshow("desen foto",desen)


cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)