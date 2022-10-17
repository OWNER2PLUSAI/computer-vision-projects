# V2.0
# With click
# ########################### VIP
# 1 click top left
# 2 click top right
# 3 click down left
# 4 click down right
#################################
import cv2 as cv
import numpy as np


circle = np.zeros((4, 2), np.int32)
counter = 0


def mousePoint(event, x, y, flags, params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        circle[counter] = x, y
        counter += 1


# every image u want
img = cv.imread("1.jpg")

while True:

    if counter == 4:
        width, hight = 500, 600
        pts1 = np.float32([circle[0], circle[1], circle[2], circle[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, hight], [width, hight]])
        metrix = cv.getPerspectiveTransform(pts1, pts2)
        imgoutput = cv.warpPerspective(img, metrix, (width, hight))
        cv.imshow("RESULT", imgoutput)

    for x in range(0, 4):
        cv.circle(img, (circle[x][0], circle[x][1]), 5, (0, 255, 0), cv.FILLED)

    cv.imshow("FIRST", img)
    cv.setMouseCallback("FIRST", mousePoint)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cv.destroyAllWindows()
