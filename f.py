# PROGRAM 6: Program on 2-d arrays addition of to matrices also find the time complexity
import time
from array import *

r = int(input("enter rows: "))
c = int(input("enter cols: "))
a = []

# Enter value for a matrix:
for i in range(r):
    t = []
    for j in range(c):
        val = int(input(f"enter a[{i}][{j}]: "))
        t.append(val)
    a.append(t)

# For printing the a matrix
for i in range(r):
    for j in range(c):
        print(a[i][j], end=" ")
    print()

# Enter value for a b matrix
b = []
for i in range(r):
    t = []
    for j in range(c):
        val = int(input(f"enter b[{i}][{j}]: "))
        t.append(val)
    b.append(t)

# For printing the b matrix
for i in range(r):
    for j in range(c):
        print(b[i][j], end=" ")
    print()

start = time.time()

Sum = []
for i in range(r):
    t = []
    for j in range(r):
        val = a[i][j] + b[i][j]
        t.append(val)
    Sum.append(t)

print("addition of matrices")

# For printing addition of matrices
for i in range(r):
    for j in range(c):
        print(Sum[i][j], end=" ")
    print()


print(time.time()-start, "is the total time of execution")