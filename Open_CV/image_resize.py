import os
import cv2

img_path = os.path.join(".","data","bird.jpg")
img = cv2.imread(img_path)
resized_img = cv2.resize(img,(640,400))

print(img.shape)
print(resized_img.shape)

cv2.imshow("img",img)
cv2.imshow("resized",resized_img)
cv2.waitKey(0)
