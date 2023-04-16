import cv2 as cv

file = "haarcascade_frontalface_default.xml"
cascade = cv.CascadeClassifier(file)

cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()

    face = cascade.detectMultiScale(img)

    for x, y, w, h in face:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 5)
        #print(x, y)

    img = cv.flip(img, 1)
    cv.imshow('frame',img)
    key = cv.waitKey(1)
    if key == ord("q") or key == ord("Q"):
        break
