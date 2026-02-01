import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/dogs.jpg')
cv.imshow('Dogs',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('Mask',mask)


#histogram for gray scale image
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#color histogram
mask = cv.bitwise_and(img,img,mask=circle)
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    plt.title('Color Histogram')
plt.figure()
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
plt.show()
cv.waitKey(0)