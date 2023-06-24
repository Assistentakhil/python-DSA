stack=[]
def push_element():
    element=input("Enter the stack:")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty,Add the element.")
    else:
        e=stack.pop()
        print(e,"Removed")
        print(stack)
def display():
    print(stack)

while True:
    print(" Select the operation 1.push  2.pop  3.display 4.quit ")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid choice")                                