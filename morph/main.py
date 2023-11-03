import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ref = None
iframe = 1
while True:
    _, frame = cap.read()
    if iframe == 10:
        ref = frame.copy()

    if ref is not None:
        cv2.imshow('ref', ref)
        diff = cv2.absdiff(ref, frame)
        cv2.imshow('diff', diff)
        d = diff.sum()
        print(d)
        if d > 38e5:
            frame[:, :, 0:2] = 0

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    iframe += 1