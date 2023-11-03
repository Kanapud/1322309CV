import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

prev = None
iframe = 1
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev is not None:

        diff = cv2.absdiff(prev, gray)
        cv2.imshow('diff', diff)
        d = diff.sum()
        print(d)
        if d > 15e5:
            frame[:, :, 0:2] = 0

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    iframe += 1

    if iframe > 50:
        prev = gray.copy()