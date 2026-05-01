import os
import cv2

img_path = os.path.join(".", "data","whiteboard.jpg")
img = cv2.imread(img_path)

cv2.line(img,(200,300),(500,100),(0,0,0),7)
cv2.rectangle(img,(400,200),(600,600),(0,0,255),9)
cv2.circle(img,(850,400),170,(255,0,0),-1)

cv2.putText(img,"Developed by Hasnaa",(660,200),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3)

cv2.imshow("Frame", img)
cv2.waitKey(0)