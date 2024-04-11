# PROGRAM 2: Program on 1-d arrays - Searching an element in an array
import time
from array import *

arrvar = array('i',[]) ##

##
n = int(input("Enter the length of the array: "))
for i in range(n):
    x = int(input("Enter the element: "))
    arrvar.append(x)
    print(arrvar)

print(arrvar)
val = int(input("Enter the element to be searched: "))

# process of searching an element and calculating the total time of execution
index = 0
for i in range(n):
    start = time.time()
    if i == val:
        print(f"Element is present at {index}th index")
        break
    index += 1
else:
    print("Element is not present")

print(time.time()-start)