# PROGRAM 5: Program on 2-d arrays like row-sum and column-sum

import time
from array import *

rc = int(input("Enter the number of rows and columns: "))
matrix = []

print("Enter the values in matrix:")

# For user input
for i in range(rc): # row count
    data = []
    for j in range(rc): # column count
        print(f"[{i}][{j}]->")
        data.append(int(input()))
    matrix.append(data)
    
# For printing the matrix 
for i in range(rc):
    for j in range(rc):
        print(matrix[i][j],end=" ")
    print()

start = time.time()

# For printing row wise sum
for i in range(rc):
    rsum = 0
    csum = 0
    for j in range(rc):
        rsum += matrix[i][j]
        csum += matrix[j][i]

    print(f"Sum of row {i+1} : {rsum}")
    print(f"Sum of column {i+1} : {csum}")

print(time.time()-start,"is the total time of execution")