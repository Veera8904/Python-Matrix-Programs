#adding of 2 matrices using numpy
import numpy as np

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = np.array(X) + np.array(Y)
print(result)




#adding of 2 matrices using sympy
from sympy import Matrix

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

matrix_x = Matrix(X)
matrix_y = Matrix(Y)

result = matrix_x + matrix_y
print(result)