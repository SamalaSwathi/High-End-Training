class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
c.deleteatbeg()
print("After deleting at begin the linked list is:")
c.printing()