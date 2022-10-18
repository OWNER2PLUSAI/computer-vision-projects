# v1.0 set show u barcode or qrcode top of rectangle

# imports
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode


# read webcam
cap = cv.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)


while True:
    success, img = cap.read()

    # find Q&Barcode
    for barcode in decode(img):
        # rectangle
        mydata = barcode.data.decode("utf-8")
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1, 1, 2)
        cv.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect

        # TEXT
        cv.putText(img, mydata, (pts2[0], pts2[1]), cv.FONT_HERSHEY_COMPLEX,
                   0.7, (255, 0, 0), 2)

    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
