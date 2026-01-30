import cv2 as cv

#reading and displaying image
img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat',img)

# reading and displaying video



capture  = cv.VideoCapture('videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
#cv2.waitKey(0)
