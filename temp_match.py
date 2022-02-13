import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
temp = cv.imread("1.jpg", 0)
w, h = temp.shape[::-1]
while True:
    ret, frame = cap.read()
    if not ret:
        print("failed in read frame")
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(frame_gray, temp, cv.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(frame, top_left, bottom_right, 255, 2)
    cv.imshow("frame", frame)
    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
