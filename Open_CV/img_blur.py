import os
import cv2

img_path = os.path.join(".", "data", "cow.jpg")
image = cv2.imread(img_path)

img = cv2.resize(image,(640,415))

k_size = 5
blurred = cv2.blur(img,(k_size,k_size))
gussian_blur = cv2.GaussianBlur(img, (k_size,k_size),5)
median_blur = cv2.medianBlur(img,k_size)

cv2.imshow("image",img)
cv2.imshow("blurred", blurred)
cv2.imshow("gussian_blur", gussian_blur)
cv2.imshow("median_blur",median_blur)
cv2.waitKey(0)