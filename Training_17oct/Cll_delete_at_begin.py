class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class cll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
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
    c.insertatend(i)
print("The linked list is:")
c.printing()
c.deleteatbeg()
print("After deleting at begin the linked list is:")
c.printing()