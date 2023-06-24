class node:
    def __init__(self,data):
        self.previous=None
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
                print("<-->",temp.data,end=" ")
                temp=temp.next
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


    
