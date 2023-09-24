import numpy as np
import matplotlib.pyplot as plt

A = plt.imread('ironman.jpg')
B = plt.imread('thanos.jpg')
print(A.shape, A.dtype, A.max())
print(B.shape, B.dtype, B.max())

def img2bp(img):
    bp = []
    for j in range(3):
        for i in range(8):
            bp.append(img[:, :, j] // (2 ** i) % 2)
    return bp

def img2bpc(img):
    bpc = []
    for j in range(3):
        for i in range(4,8):
            bpc.append(img[:, :, j] // (2 ** i) % 2)
    return bpc

def bp2img(bpc):
    height, width = bpc[0].shape
    reimg = np.zeros((height, width, 3), dtype=np.uint8)
    for j in range(3):
        for i in range(4, 8):
            reimg[:, :, j] += bpc[j * 4 + (i - 4)] * (2 ** i)
    return reimg

Ab = img2bp(A)
Bb = img2bp(B)
Abc = img2bpc(A)
Bbc = img2bpc(B)
imgA = bp2img(Abc)
imgB = bp2img(Bbc)

for i in range(24):
    plt.subplot(3, 8, i + 1)
    plt.imshow(Ab[i], cmap='gray')
plt.figure()
for i in range(24):
    plt.subplot(3, 8, i + 1)
    plt.imshow(Bb[i], cmap='gray')
plt.figure()

for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.imshow(Abc[i], cmap='gray')
plt.figure()

for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.imshow(Bbc[i], cmap='gray')
plt.figure()

plt.subplot(1,2,1);plt.imshow(imgA)
plt.subplot(1,2,2);plt.imshow(imgB)
plt.figure()

merged_image = imgA + imgB
plt.subplot(1,3,1);plt.imshow(merged_image)
plt.title("merged_image")
plt.subplot(1,3,2);plt.imshow(merged_image - imgA)
plt.title("merged_image - imgA")
plt.subplot(1,3,3);plt.imshow(merged_image - imgB)
plt.title("merged_image - imgB")
plt.show()
