import time


def selectionSort(lst):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[min_idx] > lst[j]:
                min_idx =   j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


lst = []
n = int(input("Enter the length of the list: "))
for i in range(n):
    value = int(input("Please enter the %d item: " % i))
    lst.append(value)

start = time.time()
selectionSort(lst)
print("Sorted array is:")
for i in range(n):
    print("%d" % lst[i], end=" ")

print("\n", time.time()-start, "is the total time of execution")
