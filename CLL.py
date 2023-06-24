class Node:
    def _init_(self,data):

        self.data=data
        self.next=None

#node=Node(10)
#print(node)  #<_main_.Node object at 0x00000179E4C47D50>
#print(node.data) #10
#print(node.next) #None

class CLL:
        
    def _init_(self):
        self.head=None
        self.tail=None

    def display(self):
         if self.head is None:
            print("Linked List is empty")
         else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data)
         print(temp.next.data)

    def insert_Begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head

    def delete_begining(self):
        if self.head is None:
            print("link not exist")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head

    def delete_end(self):
        temp1=self.head.next
        prev=self.head
        while temp1!=self.head:
            temp1=self.head.next
            prev=self.head
        temp1.next=None
        self.tail=prev
        self.tail.next=self.head

    def insert_pos(self,data,pos):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            if pos==1:
                insert_Begining(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new_node.next=temp.next
                temp.next=new_node

    def delete_pos(self,pos):
        if self.head is None:
            print("CLL is Empty!")
        elif pos==1:
            delete_end()
        else:
            temp=self.head.next
            prev=selself.head
            for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next
            
                
            
        
         
            

         





node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
cl=CLL()
cl.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
cl.tail=node5
cl.tail.next=cl.head

print()
print("----Insert Begin-----")
cl.insert_Begining(9)
cl.display()
print()
print("----Insert End-------")
cl.insert_end(60)
cl.display()
print()
print("----Delete Begin-----")
cl.delete_begining()
cl.display()
print()
print("----Delete End-------")
cl.delete_end()
cl.display()
print()
print("----insert_position---")
cl.insert_pos(40,3)
cl.display()
print()
print("----delete_pos--------")
cl.delete_pos(3)
cl.display()


'''print(node1)
print(node1.data)
print(node1.next)
print()
print(node2)
print(node2.data)
print(node2.next)
print()
print(node3)
print(node3.data)
print(node3.next)
print(node4)
print(node4.data)
print(node4.next)''
