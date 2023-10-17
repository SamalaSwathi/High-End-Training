class Node:
    def __init__(self,val=0):
        self.prev=None
        self.val=val
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new=Node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatbeg(i)
print("The linked list is:")
c.printing()