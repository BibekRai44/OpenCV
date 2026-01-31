import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/dogs.jpg')
cv.imshow('Dogs',img)
plt.imshow(img)
plt.show()
#to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#hsv to bgr
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

#bgr to l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('LAB',lab)

#bgr to rgb
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()



cv.waitKey(0)