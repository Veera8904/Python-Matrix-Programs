#Mutliplication of 2 matrices using numpy
import numpy as np

A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

result = np.dot(A,B)

for r in result:
    print(r)