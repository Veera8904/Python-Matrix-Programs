# n*n matrix with incrementing numbers
n = 3
matrix = []
count = 2
for i in range(n):
    row = []
    for j in range(n):
        row.append(count)
        count += 2
    matrix.append(row)

print(matrix)



#using numpy

import numpy as np
n = 4
matrix = np.ones((n, n), dtype=int)
print(matrix)