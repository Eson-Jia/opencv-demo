import numpy as np
import cv2 as cv

img = cv.imread('multi.jpeg', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
for cnt in contours:
    (x, y), radius = cv.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    cv.circle(img, center, radius, (0, 255, 0), 1)
    # cv.drawContours(img, [cnt], 0, (0, 255, 0), 1)
# cv.arcLength()
# print(M)
cv.imshow("contour", img)
while True:
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
