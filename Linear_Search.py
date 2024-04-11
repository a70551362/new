import time

lst = []
times = []
num = int(input("Enter size of the list \t"))
for n in range(num):
    numbers = int(input("Enter any number \t"))
    lst.append(numbers)

found = False
x = int(input("Enter a number to searched \t"))

start = time.time()

for i in range(len(lst)):
    if x == lst[i]:
        found = True
        print("\n%d found at position %d" % (x, i))
        break

if not found:
    print("\n%d is not in list"%x)


print(time.time()-start, "is the total time of execution")