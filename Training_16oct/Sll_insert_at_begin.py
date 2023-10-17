#insert at begin
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=sll()
for i in l:
    c.insertatbegin(i)
c.printing()
