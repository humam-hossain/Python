import cv2 as cv

img = cv.imread("/home/painkiller/github_repo/Python/opencv/Photos/cat_larges.jpg")

cv.imshow("Cat", img)

cv.waitKey(0)

# Reading videos
# capture = cv.VideoCapture("/home/painkiller/github_repo/Python/opencv/Videos/dog.mp4")

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)

#     if cv.waitKey(20) & 0xFF ==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()