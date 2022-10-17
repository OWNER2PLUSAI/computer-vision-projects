import cv2 as cv
import numpy as np
#############################
width = 500
hight = 600
#############################

img = cv.imread("1.jpg")
pts1 = np.float32([[343,67] ,[662,67] ,[292,463] ,[724,457]])
pts2 = np.float32([[0,0],[width,0],[0, hight],[width,hight]])
metrix = cv.getPerspectiveTransform(pts1,pts2)

imgoutput = cv.warpPerspective(img, metrix, (width,hight))


for x in range(0, 4):
    cv.circle(img ,(int(pts1[x][0]) ,int(pts1[x][1])) ,5 ,(0,0,255) ,cv.FILLED)


cv.imshow("FIRST", img)
cv.imshow("RESULT", imgoutput)
cv.waitKey(0)
cv.destroyAllWindows()