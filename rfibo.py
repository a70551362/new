# Program to find fibonacci using recursive approach

def recur_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (recur_fibo(n-1)+recur_fibo(n-2))


n = int(input("How many terms? "))
if n <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(recur_fibo(i), " ", end=" ")
