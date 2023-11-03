import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

prev = None
L1 = 50
th = 10
iframe = 1
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev is not None:
        diff = cv2.absdiff(prev[:, L1:L1+th], gray[:, L1:L1+th])
        cv2.imshow('diff', diff)
        d = diff.sum()
        print(d)
        if d > 1e4:
            frame[:, L1:L1 + th, 0:2] = 0
        else:
            frame[:, L1:L1 + th, [0, 2]] = 0

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    iframe += 1

    if iframe > 50:
        prev = gray.copy()