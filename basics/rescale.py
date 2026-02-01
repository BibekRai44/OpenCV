import cv2 as cv
 
img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat',img)
 
#scaling frame
def rescaleFrame(frame,scale=0.75):
    # works for image, video and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img,scale=0.5)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #only for live video
    capture.set(3,width)
    capture.set(4,height)

capture  = cv.VideoCapture('videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.5)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break