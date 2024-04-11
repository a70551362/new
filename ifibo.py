# Program to find fibonacci using iterative approach

def fib(n):
    prev = 0
    temp = 1
    if n == 1:
        print(prev,"",end=" ")
    else:
        print(prev," ",end=" ")
        print(temp," ",end=" ")
    for i in range(2,n):
        add = prev + temp
        prev = temp
        temp = add
        print(add,"",end=" ")

n = int(input("Enter total no. of terms: "))
if n <= 0:
    print("Please enter a positive integer greater than 0")
else:
    print("Fibonacci numebr using iterative method")
    fib(n)

