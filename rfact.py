# Program to find factorial using recursive approach

def recu_factorial(n):
    if n == 1:
        return n
    else:
        return n * recu_factorial(n-1)
    
num = int(input("Enter a number: "))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    print("The factorial of",num,"is",recu_factorial(num))

    