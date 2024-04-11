import time

def BinarySearch(lst,key):
    low = 0
    high = len(lst) - 1
    Found = False
    while low <= high and not Found:
        mid = (low + high) // 2
        if key == lst[mid]:
            Found = True
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if Found == True:
        print("Key is found")
    else:
        print("Key is not found")
lst = []
num = int(input("Enter the size of the list \t"))
for n in range(num):
    numbers = int(input("Enter any number \t"))
    lst.append(numbers)

lst.sort()
print("Sorted list")
print(lst)

key = int(input("Enter a number to searched \t"))
start = time.time()
BinarySearch(lst,key)
print(time.time()-start, "is the total time of execution")
