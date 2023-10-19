class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    printing(root.left)
    printing(root.right)
    print(root.val)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(4)

q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.val)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)