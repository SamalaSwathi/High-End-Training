#insert a node to the list
class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def create(self,x):                                 #To add nodes at the last
        if(self.head==None):
            self.head=node(x) 
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
b=cse()
b.create(10)
b.create(20)
b.create(30)
b.create(40)
print(b.head.data)
print(b.head.next)
print(b.head.next.data)
print(b.head.next.next)
print(b.head.next.next.data)
print(b.head.next.next.next)
print(b.head.next.next.next.data)
print(b.head.next.next.next.next)