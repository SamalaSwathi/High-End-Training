#To insert a node in the single linked list
class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def create(self,x):                                 
        if(self.head==None):
            self.head=node(x) 
        else:
            temp=self.head
            while(temp.next!=None):                    #To add node at the front
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
b=cse()
b.create(20)
b.create(30)
b.create(40)
b.add_front(10)
print(b.head.data)
print(b.head.next)
print(b.head.next.data)
print(b.head.next.next)
print(b.head.next.next.data)
print(b.head.next.next.next)
print(b.head.next.next.next.data)
print(b.head.next.next.next.next)