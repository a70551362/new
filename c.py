# PROGRAM 3: Finding maximum and minimum element in array
import time
from array import *

arrvar = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the element: "))
    arrvar.append(x)
    print(arrvar)

max_arr = min_arr = arrvar[0]
start = time.time()
for i in arrvar:
    if i > max_arr:
        max_arr = i
    if i < max_arr:
        min_arr = i


print(max_arr, "is the maximum element in the array")
print(min_arr, "is the minimum element in the array")
print(time.time()-start)
