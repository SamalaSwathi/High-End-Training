#To create two nodes in single linked list
class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self,k):
        self.head=None
    def qwer(self,x):                            #Single Linked list with 2 nodes
        if(self.head==None):
            self.head=node(x) 
        else:
            self.head.next=node(x)
a=cse(80)                                         
b=cse(12)
b.qwer(20)
b.qwer(30)
print(b.head.data)
print(b.head.next)
print(b.head.next.data)
print(b.head.next.next)