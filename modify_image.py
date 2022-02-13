import cv2.cv2 as cv

image = cv.imread("test.png")

print(image.shape)
print(image.size)
print(image.dtype)

some = image[:500, :500]
cv.imshow("ddd", some)
cv.imshow("first", image[:, :, 0])
cv.imshow("second", image[:, :, 1])
cv.imshow("third", image[:, :, 2])

e1 = cv.getTickCount()
for i in range(5,49,2):
    image = cv.medianBlur(image,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )

cv.imshow("four", image)

while cv.waitKey(10) != ord('q'):
    continue
