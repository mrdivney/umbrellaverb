''' Edith Cam'''
import cv2
import winsound
Edith_Cam = cv2.VideoCapture(0)
while Edith_Cam.isOpened:
    ret, frame1 = Edith_Cam.read()
    ret, frame2 = Edith_Cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, rolling = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(rolling, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
    for small_movement in contours:
        if cv2.contourArea(small_movement) < 4000:
            continue
        x,y,w,h = cv2.boundingRect(small_movement)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        winsound.Beep(500, 200)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Edith-Cam', frame1)