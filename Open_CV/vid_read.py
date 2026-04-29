import os
import cv2

vid_path = os.path.join(".", "data", "cow.mp4")
video = cv2.VideoCapture(vid_path)

ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow("Frame", frame)
        cv2.waitKey(30)


video.release()
cv2.destroyAllWindows()