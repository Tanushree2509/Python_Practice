'''
import numpy as np
A=[2,4,6]
B=[1,2,3]
matrix_A = np.mat(A)
matrix_B = np.mat(B)
print(matrix_A * matrix_B)
'''

import numpy as np
A = np.array([2, 4, 6]).reshape(1, 3)  # 1x3
B = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 3x3
print(A @ B)  # matrix multiply