import cv2 as cv

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat',img)

#converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur the image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#detecting edges

canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

canny_blur = cv.Canny(blur,125,175)
cv.imshow('Canny Edges blur',canny_blur)

#dilating the image
dilated = cv.dilate(canny,(7,7),iterations = 3)
cv.imshow('Dialted',dilated)

# eroding the image
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropped  = img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)