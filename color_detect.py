import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    if ret:
        hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower = np.array([150,140,10])
        upper = np.array([179,255,255])
        mask = cv2.inRange(hsv_image,lower,upper)
        edges = cv2.Canny(mask,75,150)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
        if lines is not None:
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
