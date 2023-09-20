import numpy as np
import matplotlib.pyplot as plt
import cv2

# # binary image
# bin = np.full((100, 256), 0, dtype=np.uint8) #Full สร้างของที่มีมิติ สูงกับกว้าง
# for i in range(256):
#     bin[:, i] = i
# plt.imshow(bin, cmap='gray') #Display  ไม่ได้รองรับ boolean รองรับ int float
# plt.show() #Display

# #Array
# bin = np.full((100, 256, 3), 0, dtype=np.float32)
# bin[:, :, 0:3:2] = 1
# plt.imshow(bin, cmap='gray')
# plt.show()
# # meaning [: = all] - [3:6 = 3,4,5 (ตัวหน้า include ตัวหลัง exclude ไม่เอา)] - [3:10:2 = 3,5,7,9 คือ เริ่ม 3 ถึง 10 แต่ +ทีละ 2]
# # [:4 = 0,1,2,3] - [3: คือเริ่มจาก 3 ไปถึงตัวสุดท้าย] - [-1 = Last ตัวสุดท้าย]

#ThaiFlag
thai = np.full((600, 800, 3), 0, dtype=np.uint8)
thai[:100, :] =[165, 25, 49]
thai[100:200, :] = [244, 245, 248]
thai[200:400, :] = [45, 42, 74]
thai[400:500, :] = [244, 245, 248]
thai[500:600, :] = [165, 25, 49]

#FranceFlag
france = np.full((600, 900, 3), 0, dtype=np.uint8)
france[:, :300] =[0,85,164]
france[:, 300:600] = [255,255,255]
france[:, 600:] = [239,65,53]

#GermanFlag
german = np.full((600, 900, 3), 0, dtype=np.uint8)
german[:200, :] = [0,0,0]
german[200:400, :] = [255,0,0]
german[400:, :] = [255,204,0]

#JapanFlag
japan = np.full((600, 900, 3), 255,  dtype=np.uint8)
for x in range(japan.shape[1]): #Shape คงอัตราส่วนไว้
    for y in range(japan.shape[0]):
        if (x-japan.shape[1] / 2)**2 + (y-japan.shape[0] / 2)**2 <= (3 / 5 * japan.shape[0] / 2) **2:
            japan[y, x] = [188, 0, 45]

plt.subplot(2, 2, 1)
# plt.imshow(255-thai) Negative image
plt.imshow(thai)
plt.axis(False)

plt.subplot(2, 2, 2)
plt.imshow(france)
plt.axis(False)

plt.subplot(2, 2, 3)
plt.imshow(german)
plt.axis(False)

plt.subplot(2, 2, 4)
plt.imshow(japan)
plt.axis(True)

plt.show()