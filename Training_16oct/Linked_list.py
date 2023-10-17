class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o1.next=node(2)
o1.next.next=node(3)
print(o1.val,o1.next.val,o1.next.next.val)