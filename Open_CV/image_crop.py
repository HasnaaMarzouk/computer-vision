import os
import cv2

img_path = os.path.join(".", "data", "bird.jpg")
img = cv2.imread(img_path)
print(img.shape)

cropped_img = img[50:700,100:700]


cv2.imshow("image", img)
cv2.imshow("cropped", cropped_img)
cv2.waitKey(0)

