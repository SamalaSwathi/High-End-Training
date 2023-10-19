class Node:
    def __init__(self,val=0):
        self.prev=None
        self.val=val
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=Node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def printing(self):
        print(self.head.val)
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=cll()
for i in l:
    c.insertatbeg(i)
print("The linked list is:")
c.printing()
