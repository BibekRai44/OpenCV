import cv2 as cv

img = cv.imread('photos/dogs.jpg')
cv.imshow('Dogs',img)

#averaging

average = cv.blur(img,(7,7))
cv.imshow('Averaging',average)

# gaussian blur

gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

#median blur
median = cv.medianBlur(img,7)
cv.imshow('Median Blur',median)

#bilaterial blur
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral Blur',bilateral)
cv.waitKey(0)
