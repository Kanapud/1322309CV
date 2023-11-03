import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
U = (100, 255, 100)
L = (0, 100, 0)
draw = False
canvas = np.zeros((int(h), int(w), 3), dtype=np.uint8)
while True:
    _, frame = cap.read()
    mask = cv2.inRange(frame, L, U)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0 and cv2.contourArea(contour) > 200:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            if draw:
                cv2.circle(canvas, (cX, cY), 7, (0, 0, 255), -1)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('canvas', canvas)
    key = cv2.waitKey(1)
    if key & 0xff == ord('p'):
        draw = not draw
        print(draw)