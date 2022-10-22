#v2.0 set show u barcode or qrcode top of rectangle 


#imports
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

#read webcam
cap = cv.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

# read private barcode and qrcode in db(mysql)
with open("D:\Python\Github\computer-vision-projects\QRCode_BarCode\Authentication\myQRfile.text") as f:
    mydataList = f.read().splitlines()

while True:
    success , img = cap.read()
    
    for barcode in decode(img):
        mydata = barcode.data.decode("utf-8")
        
        # condition for if code u show that is db show green Authorized else show red Un-Authorized
        if mydata in mydataList:
            myOutPut = "Authorized"
            myColor = (0,255,0)
        else:
            myOutPut = "Un-Authorized"
            myColor = (0,0,255)
        
        # rectangle
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv.polylines(img,[pts],True,(255,0,255), 5)
        pts2 = barcode.rect
        
        #show Authorized or Un-Authorized
        cv.putText(img,myOutPut, (pts2[0],pts2[1]) ,cv.FONT_HERSHEY_COMPLEX,
                   0.7 ,myColor ,2)
        
    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break