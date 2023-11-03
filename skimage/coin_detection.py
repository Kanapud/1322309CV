import skimage
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage.filters import threshold_otsu
from skimage.morphology import dilation, erosion, remove_small_holes
from skimage.measure import regionprops, label

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
binary_image = None
while True:
    _, frame = cap.read()

    if len(pts2) == 4:
        pts2 = np.float32(pts2)
        T = cv2.getPerspectiveTransform(pts2, pts1)
    if T is not None:
        frame = cv2.warpPerspective(frame, T, (500, 500))
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
        binary_image = cv2.bitwise_not(binary_image)

        cv2.imshow('binary', binary_image)
        binary_image = dilation(binary_image, np.ones((3, 3)))
        binary_image = remove_small_holes(binary_image, area_threshold=90)
        binary_image = erosion(binary_image, np.ones((3, 3)))

        binary_image = label(binary_image)
        selected = []
        ten_bath = []
        five_bath = []
        one_bath = []
        for r in regionprops(binary_image):
            w = abs(r.bbox[0] - r.bbox[2])
            h = abs(r.bbox[1] - r.bbox[3])

            wh_ratio = w / h
            if r.area > 1e3 and 0.8 <= wh_ratio <= 1.2:

                if 64 <= w :
                    ten_bath.append(r.label)
                if 53 <= w <= 63 :
                    five_bath.append(r.label)
                if w <= 52 :
                    one_bath.append(r.label)
                selected.append(r.label)

        print('number of coins = ', len(selected), 'ten baht = ',len(ten_bath), 'five baht = ',len(five_bath), 'one baht = ',len(one_bath))
        price = (len(ten_bath)*1)+(len(five_bath)*5)+(len(one_bath)*1)
        print('price =', price, ' baht')
    cv2.imshow('frame', frame)
    cv2.waitKey(1)