class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class doublelinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print('Linked list is Empty!')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
                
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None

    def delete_position(self,position):
        prev=self.head
        temp=self.head.next
        for i in range(1,position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.prev=prev
    

    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None

obj=doublelinkedlist()
node1=node(20)
obj.head=node1
node2=node(30)
node1.next=node2
node2.prev=node1
node3=node(40)
node2.next=node3
node3.prev=node2
node4=node(50)
node3.next=node4
node4.prev=node3
obj.display()
print("\nDelete begin")
obj.delete_begining()
obj.display()
print()
print("\nDelete middel")
obj.delete_position(3)
obj.display()
print()
print("\nDelete end")
obj.delete_end()
obj.display()
print()
                    
