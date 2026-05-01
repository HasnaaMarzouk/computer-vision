import cv2
import numpy as np
from utils import get_limits
from PIL import Image

blue = [0, 255, 255]

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=blue)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()