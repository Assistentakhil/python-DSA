queue=[]


def enqueue():
    element=input("Enter the queue:")
    queue.append(element)
    print(queue)
    
def dequeue():
    if not queue:
        print("queue is empty,Add the element.")
    else:
        e=queue.pop()
        print(e,"Removed")
        print(queue)

def display():
    print(queue)

while True:
    print(" Select the operation 1.enqueue 2.dequeue  3.display 4.quit ")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid choice")                                
