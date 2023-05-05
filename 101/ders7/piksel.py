import cv2
import numpy as np 

img1 = cv2.imread("101/ders7/mor.jpeg")
img2 = cv2.imread("101/ders7/yesil.jpg")

# print(img1[100,200]) bgr değerlerini okuyoruz o pikseldeki
# print(img2[200,300])

part1 = img1[0:300,0:200]
part2 = img2[0:300,0:200]

cv2.imshow("new",part1)
cv2.imshow("new2",part2)

total = cv2.add(part1,part2)
cv2.imshow("total",total)

totalweighted = cv2.addWeighted(part1,0.2,part2,0.8,0)
cv2.imshow("total weigh",total)


cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)
