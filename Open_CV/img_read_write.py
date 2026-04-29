import cv2
import os

# read image
img_path = os.path.join('.', "data", "bird.jpg")
img = cv2.imread(img_path)

# write image
cv2.imwrite(os.path.join('.','data',"bird_out.jpg"), img)

# visualise image
cv2.imshow("Bird", img)
cv2.waitKey(0) 
