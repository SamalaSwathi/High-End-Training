class Node:
    def __init__(self,val=0):
        self.prev=None
        self.val=val
        self.next=None
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
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
    def reverse(self):
        temp=self.tail
        while(temp!=None):
            print(temp.val)
            temp=temp.prev
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
print("The reverse traversal of the linked list is:")
c.reverse()
