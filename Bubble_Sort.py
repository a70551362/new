import time


def bubbleSort(lst):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)


lst = []
n = int(input("Enter length of the list: "))
for i in range(n):
    value = int(input("Please enter the %d item: " % i))
    lst.append(value)

start = time.time()
bubbleSort(lst)

print("Sorterd array is:")
for i in range(n):
    print("%d" % lst[i], end=" ")

print("\n", time.time()-start, "is the total time of execution")
