#!/bin/python3

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and live video 

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread("/home/painkiller/github_repo/Python/opencv/Photos/cat_large.jpg")
img_resize  = rescaleFrame(img, scale=0.2)

cv.imshow("Cat", img)
cv.imshow("Cat resized", img_resize)

# cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture("/home/painkiller/github_repo/Python/opencv/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()