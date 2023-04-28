import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)

B = A.copy()
print(B)

A = np.zeros((2, 3))
A

B = np.ones((3, 2))
B

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.zeros_like(A)
B

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.ones_like(A)
B

A = np.eye(3)
A

From = 2.5
To = 7
Step = 0.5
A = np.arange(From, To, Step)
A

A = np.arange(5)
A

A = np.arange(10, 15)
A

A = np.zeros((2, 3), 'int')
A

B = np.ones((3, 2), 'complex')
B

A = np.ones((3, 2))
B = A.astype('str')
B

A = np.array([[1, 2, 3], [4, 5, 6]])
A[1, 1]
A = np.array([[1, 2, 3], [4, 5, 6]])
A[1]

A = np.array([[1, 2, 3], [4, 5, 6]])
A[1][1]

A = np.array([[1, 2, 3], [4, 5, 6]])
A[1, :]

A = np.array([[1, 2, 3], [4, 5, 6]])
A[:, 1]

A = np.arange(5)
print(A)
A[-1]

A = np.arange(5)
print(A)

A[[0, 1, -1]]
A = np.arange(5)
print(A)
A[0:4:2]

A = np.arange(5)
print(A)
A[0:4]

A = np.arange(5)
print(A)
A[:4]

A = np.arange(5)
print(A)
A[-3:]

A = np.array([[1, 2, 3], [4, 5, 6]])
B = A[:, ::-1]
print("A", A)
print("B", B)

print(A)
B[0, 0] = 0
print(A)

A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.copy()[:, ::-1]
print("A", A)
print("B", B)

A = np.array([[1, 2, 3], [4, 5, 6]])
I = np.array([[False, False, True], [ True, False, True]])
A[I]

A = np.array([[1, 2, 3], [4, 5, 6]])
I = np.array([[False, False, True], [ True, False, True]])
A[I] = 0
print(A)



A = np.array([[1, 2, 3], [4, 5, 6]])

I1 = np.array([[False, False, True], [True, False, True]])
I2 = np.array([[False, True, False], [False, False, True]])

B = A.copy()
C = A.copy()
D = A.copy()

B[np.logical_and(I1, I2)] = 0
C[np.logical_or(I1, I2)] = 0
D[np.logical_not(I1)] = 0

print('B\n', B)
print('\nC\n', C)
print('\nD\n', D)



A = np.array([[1, 2, 3], [4, 5, 6]])

I1 = np.array([[False, False, True], [True, False, True]])
I2 = np.array([[False, True, False], [False, False, True]])

A[I1 & (I1 | ~ I2)] = 0

print(A)

A = np.array([[1, 2, 3], [4, 5, 6]])
print('A before\n', A)

I = A > 3
print('I\n', I)

A[np.logical_or(A < 2, A > 4)] = 0
print('A after\n', A)


A = np.arange(24)
B = A.reshape(4, 6)
C = A.reshape(4, 3, 2)
print('B\n', B)
print('\nC\n', C)


A = np.arange(24)
C = A.reshape(4, 3, 2)

print(C.ndim, C.shape, len(C.shape), A.size)


A = np.array([[1, 2, 3], [4, 5, 6]])
A.ravel()

A = np.array([[1, 2, 3], [4, 5, 6]])
A.reshape(3, 2)





A = np.arange(24)
B = A.reshape(4, -1)
C = A.reshape(4, -1, 2)

print(B.shape, C.shape)


A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.reshape(-1)
print(B.shape)