import cv2 as cv2

#reading and displaying image
#img = cv2.imread('photos/cat1.jpg')
#cv2.imshow('Cat',img)

# reading and displaying video
capture  = cv2.VideoCapture('videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video',frame)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
#cv2.waitKey(0)
