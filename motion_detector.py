import cv2, time, pandas
from datetime import datetime

first_frame = None

video = cv2.VideoCapture(0)

while True:


    check, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts,_) = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,z) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+z),(0,255,0),3)






    #cv2.imshow("capturing",gray)
    #cv2.imshow("press q to cancel",delta_frame)
    #cv2.imshow("thresh frame",thresh)
    cv2.imshow("press q to cancel",frame)


    key = cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
