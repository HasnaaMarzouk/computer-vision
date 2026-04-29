import os
import cv2

img_path = os.path.join(".","data","bird.jpg")
image = cv2.imread(img_path)
img = cv2.resize(image,(640,400))

img_conv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("bgr_img", img)
cv2.imshow("rgb_img", img_conv)
cv2.imshow("gray_img", img_gray)
cv2.imshow("hsv_img", img_hsv)

cv2.waitKey(0)