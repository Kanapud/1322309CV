import skimage
import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage import data
from skimage.filters import threshold_otsu
from skimage.morphology import dilation, erosion, remove_small_holes
from skimage.measure import regionprops, label      # regionprops ใช้ตรวจจับสิ่งของได้ เช่นอันนี้กลม อันนี้เหลี่ยม

A = data.coins()
T = threshold_otsu(A)
B = A > T + 20 # threshold

B = dilation(B, np.ones((3, 3))) # ทำให้ขอบของวัตถุที่เห็นชัดขึ้น

B = remove_small_holes(B, area_threshold=90) # ลบส่วนที่เป็นรู หรือส่วนที่เป็นรูปกลมเล็กๆออก

B = erosion(B, np.ones((3, 3))) # ทำให้ขอบของวัตถุที่เห็นชัดขึ้น

B = label(B) # ใส่เลขลงไปในวัตถุที่เห็นได้

plt.subplot(1, 3, 1)
plt.imshow(A, cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(B, cmap='gray')
C = np.zeros_like(B)
selected = []
for r in regionprops(B):
    w = abs(r.bbox[0] - r.bbox[2]) # คำนวณความกว้างของวัตถุ
    h = abs(r.bbox[1] - r.bbox[3]) # คำนวณความสูงของวัตถุ
    wh_ratio = w / h
    if r.area > 1e3 and 0.8 <= wh_ratio <= 1.2: # ถ้าขนาดของวัตถุมากกว่า 1e3 และ อัตราส่วนของความกว้างและความสูงอยู่ในช่วง 0.8 - 1.2
        print(w / h)
        plt.plot(r.centroid[1], r.centroid[0], 'xr') # วาดจุดที่เป็นศูนย์กลางของวัตถุ
        selected.append(r.label) # เก็บเลขวัตถุที่เป็นวัตถุที่เราต้องการ
        C[B == r.label] = 1

print("number of coins: ", len(selected)) # แสดงจำนวนวัตถุที่เป็นวัตถุที่เราต้องการ
plt.subplot(1, 3, 3)
plt.imshow(C, cmap='gray')
plt.show()