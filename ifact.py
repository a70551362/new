# Program to find factorial using iterative approach

def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


n = int(input("Enter a number: "))
if n < 0:
    print("Please enter a positive integer")
else:
    print("Using iterative method factorial is", factorial(n))
