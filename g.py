# PROGRAM 7: Program to create a list-based stack and perform various stack operations

stack = []

MAX_CAPACITY = 3

def push():
    if(len(stack)==MAX_CAPACITY):
        print("Stack Overflow...!!")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop_element():
    if(len(stack)==0):
        print("Stack is underflow")
    else:
        e = stack.pop()
        print("removed element",e)
        print(stack)

def top_element():
    top = stack[-1]
    print("Top of stack is ",top)

def is_empty():
    if stack == []:
        print("Stack is empty")
    else:
        print("Stack is not empty")
    
while True:
    print("Select the operation 1.push 2.pop 3.top 4.isempty 5.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        top_element()
    elif choice == 4:
        is_empty()
    elif choice == 5:
        break
    else:
        print("Enter the correct operation")
