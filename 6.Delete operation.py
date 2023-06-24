class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print('Linked list is Empty!')
        else:
            temp=self.head
            while temp:
                print("->",temp.data,end=" ")
                temp=temp.next


    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_position(self,position):
        prev=self.head
        temp=self.head.next
        for i in range(1,position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next    


    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

obj=singlelinkedlist()
n=Node(20)
obj.head=n
n1=Node(30)
obj.head.next=n1
n2=Node(40)
n1.next=n2
n3=Node(50)
n2.next=n3
n4=Node(60)
n3.next=n4
n5=Node(70)
n4.next=n5
obj.display()
   
print("\nDelete_begining")    
obj.delete_begining()
obj.display()
print()

print("\n Delete_middle")
obj.delete_position(3)
obj.display()
print()

print("\nDelete_end")
obj.delete_end()
obj.display()
print()
