import os
import cv2
import numpy as np


img_path = os.path.join(".","data","basketball_player.jpg")
img = cv2.imread(img_path)


img_edge = cv2.Canny(img,200,100)

img_edge_dilate = cv2.dilate(img_edge,
                              np.ones((3,3), dtype=np.int8))

img_edge_erode = cv2.erode(img_edge_dilate,
                              np.ones((3,3), dtype=np.int8))

cv2.imshow("img_edge",img_edge)
cv2.imshow("img_edge_erode",img_edge_erode)
cv2.imshow("img",img)
cv2.imshow("img_edge_dilate", img_edge_dilate)
cv2.waitKey(0)











