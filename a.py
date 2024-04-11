# PROGRAM 1: Program on 1-d arrays - Sum of elements of array
import time
from array import *

arrvar = array('i', []) # intialising array with list of integers

# adding elements in that same list
n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input("Enter the element: "))
    arrvar.append(x)
    print(arrvar)

start = time.time() # start time of the execution

# function to calculate the sum of elements in the array
def arrsum(arrvar):
    x = 0
    for i in arrvar:
        x += i
    return x

ans = arrsum(arrvar)
print(ans)
print(time.time()-start) # give the time of execution
