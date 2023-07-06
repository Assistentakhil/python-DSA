class bst:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

    def insert_node(self,data):
        if self.key is None:
            return
        if self.key==data:
            return
        if self.key>data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=bst(data)
        else:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=bst(data)


    def pre_order(self):
        print(self.key,end=" ")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
            
    def in_order(self):
        if self.l_child:
            self.l_child.in_order()
        print(self.key,end=" ")
        if self.r_child:
            self.r_child.in_order()

    def post_order(self):
        if self.l_child:
            self.l_child.post_order()
        if self.r_child:
            self.r_child.post_order()
        print(self.key,end=" ")




    def delete(self,data):
        if self.key is None:
            print("Tree is Empty")
        else:
            if data<self.key:
                if self.l_child:
                    self.l_child=self.l_child.delete(data)
                else:
                    print(" node is not present")
            elif data>self.key:
                if self.r_child:
                    self.r_child=self.r_child.delete(data)
                else:
                    print(" node is not present")   
            else:
                if self.l_child is None:
                    temp=self.r_child
                    self=None
                    return temp
                if self.r_child is None:
                    temp=self.l_child
                    self=None
                    return temp
                n=self.r_child
                while n.l_child:
                    n=n.l_child
                self.key=n.key
                self.r_child=self.r_child.delete(n.l_child)
        return self  

                



                

root=bst(5)
root.insert_node(0)
root.insert_node(1)
root.insert_node(2)
root.insert_node(3)
root.insert_node(4)
root.insert_node(6)
root.insert_node(7)
root.insert_node(8)
root.insert_node(9)
root.insert_node(10)
root.pre_order()
print()
root.in_order()
print()
root.post_order()
print()
root.delete(6)
print()
