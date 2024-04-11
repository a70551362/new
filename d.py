# PROGRAM 4: Find the number of even and odd numbers in an array
import time
from array import *

arrvar = array('i',[])

n = int(input("Enter the length of the array: "))
for i in range(n):
    x = int(input("Enter the elements: "))
    arrvar.append(x)
    print(arrvar)

even = odd = 0
start = time.time()
for i in arrvar:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    
print(even, "Number of even elements in the array")
print(odd, "Number of odd elements in the array")
print(time.time()-start,"is the total time of execution")