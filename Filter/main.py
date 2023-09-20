import matplotlib.pyplot as plt
import numpy as np

def padding(A, filter, method='zero'):
    p0 = filter.shape[0] // 2
    p1 = filter.shape[1] // 2
    if method == 'zero':
        B = np.zeros((A.shape[0] + 2 * p0, A.shape[1] + 2 *p1))
        B[p0:p0+A.shape[0], p1:p1+A.shape[1]] = A
        return B[A.shape[0] - p0: (A.shape[0] * 2) + p0, A.shape[0] - p1: (A.shape[0] * 2) + p1]

    elif method == 'mirror':
        Afr = A[::-1, :]
        Afc = A[:, ::-1]
        Afrc = A[::-1, ::-1]
        B0 = np.hstack((Afrc,Afr,Afrc))
        B1 = np.hstack((Afc,A,Afc))
        B = np.vstack((B0,B1,B0))
        return B[A.shape[0] - p0: (A.shape[0] * 2) + p0, A.shape[0] - p1: (A.shape[0] * 2) + p1]

    elif method == 'circular':
        B = np.hstack((A,A,A))
        B = np.vstack((B,B,B))
        return B[A.shape[0] - p0: (A.shape[0] * 2) + p0, A.shape[0] - p1: (A.shape[0] * 2) + p1]

def filtering(A, filter, method='zero'):
    B = padding(A, filter, method)
    C = np.zeros_like(A)
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            C[i, j] = np.sum(B[i:i+filter.shape[0], j:j+filter.shape[1]] * filter)
    return C

A = np.random.randint(0,15,(3,3))
average_filter = 1/9 * np.ones((5,5))
print('A')
print(A)
print('zero')
print(padding(A,average_filter,method='zero'))
print('mirror')
print(padding(A,average_filter,method='mirror'))
print('circular')
print(padding(A,average_filter,method='circular'))

"""
average_filter = 1/121 * np.ones((11,11))
A = plt.imread('leaf.jpg') / 255.
A = A[:, :, 1]
B = filtering(A, average_filter, 'zero')
plt.subplot(1, 2, 1)
plt.imshow(A)
plt.subplot(1, 2, 2)
plt.imshow(B)
plt.show()
"""