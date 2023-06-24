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
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_position(self,position,data):
        new_Node=Node(data)
        temp=self.head
        for i in range(0,position-1):
            temp=temp.next
        new_Node.next=temp.next
        temp.next=new_Node
        
    def insert_end(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.next=None
        



obj=singlelinkedlist()
obj.insert_beginning(10)
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
print("\t")
print("\t")
print("\nBEGIN")
print("\t")
obj.insert_beginning(10)
obj.display()
print("\t")
print("\t")
print("\n MIDDLE")
print("\t")
obj.insert_position(3,100)
obj.display()
print("\t")
print("\t")
print("\nEND")
print("\t")
obj.insert_end(80)
obj.display()
