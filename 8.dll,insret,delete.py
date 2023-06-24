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
                
    def insert_begining(self,data):
        new_node=node(data)
        temp=self.head
        temp.pervious=new_node
        new_node.next=temp
        self.head=new_node
        
    def insert_position(self,position,data):
        new_node=node(data)
        temp=self.head
        for i in range(0,position-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        new_node.previous=temp.next

    def insert_end(self,data):
        new_node=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
        new_node.previous=temp.next
            
            

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
print("\nInsert begin")
obj.insert_begining(10)
obj.display()
print()
print("\nInsert middle")
obj.insert_position(3,390)
obj.display()
print()
print("\nInsert end")
obj.insert_end(80)
obj.display()
print()
    
