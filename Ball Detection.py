import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    img2=img.copy()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,250,param1=50,param2=30,minRadius=0,maxRadius=0)
    if circles is not None:
        data=np.uint16(np.around(circles))
        for (x,y,r) in data[0,:]:
            cv2.circle(img2,(x,y),r,(52,235,70),5)
            cv2.circle(img2,(x,y),1,(0,255,100),-1)
    cv2.imshow("res",img2)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
