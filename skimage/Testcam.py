import cv2
import numpy as np

pts1 = np.float32([[0, 0], [500, 0], [500, 500], [0, 500]])

pts2 = []
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        pts2.append((x, y))

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', on_click)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
T = None
while True:
    _, frame = cap.read()

    if len(pts2) == 4:
        pts2 = np.float32(pts2)
        T = cv2.getPerspectiveTransform(pts2, pts1)
    if T is not None:
        frame = cv2.warpPerspective(frame, T, (500, 500))

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

#TestCamera
# pts1 = np.float32([[0, 0], [500, 0], [500, 500], [0, 500]])
#
# pts2 = []
# def on_click(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, y)
#         pts2.append((x, y))
#
# cv2.namedWindow('frame')
# cv2.setMouseCallback('frame', on_click)
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# T = None
# while True:
#     _, frame = cap.read()
#
#     if len(pts2) == 4:
#         pts2 = np.float32(pts2)
#         T = cv2.getPerspectiveTransform(pts2, pts1)
#     if T is not None:
#         frame = cv2.warpPerspective(frame, T, (500, 500))
#
#     cv2.imshow('frame', frame)
#     cv2.waitKey(1)