import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

# set address of ur movie
cap = cv.VideoCapture(" ############## UR movie Address ")
 
# Need  myQRfile.text address in ur pc vip
with open("  /////myQRfile.text") as f:
    mydataList = f.read().splitlines()


if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv.VideoWriter('outpy.mp4',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
while(True):
  ret, img = cap.read()
 
  if ret == True: 
      for barcode in decode(img):
        mydata = barcode.data.decode("utf-8")
        
        # condition for if code u show that is db show green Authorized else show red Un-Authorized
        if mydata in mydataList:
            myOutPut = "Authorized"
            myColor = (0,255,0)
        else:
            myOutPut = "Un-Authorized"
            myColor = (0,0,255)
        
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv.polylines(img,[pts],True,(255,0,255), 5)
        pts2 = barcode.rect
        cv.putText(img,myOutPut, (pts2[0],pts2[1]) ,cv.FONT_HERSHEY_COMPLEX,
                   0.7 ,myColor ,2)
                   
        # write video 
        out.write(img)

        # cv.imshow('frame',img)
 
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv.destroyAllWindows()