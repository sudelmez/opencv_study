import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('101/perspective/view.jpg')

# Görüntünün orijinal boyutları
h, w = img.shape[:2]

# Perspektif dönüşümü uygulanacak dörtgenin köşe noktaları (örneğin, görüntünün dört köşesi)
src_points = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])

# Hedef dörtgenin köşe noktaları
dst_points = np.float32([[0, 0], [w-1, 0], [int(0.33*w), h-1], [int(0.66*w), h-1]])

# Perspektif dönüşüm matrisini hesapla
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Perspektif dönüşümünü uygula
result = cv2.warpPerspective(img, matrix, (w, h))

# Sonucu göster
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
