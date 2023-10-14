#Class and Objects demo2
#Constructor
class cse:
    x=10
    def __init__(self):
        self.y=30
    def qwer(self):             #Here x is a static variable and y is a non-static variable
        print("Hi")                    #so we need to call y as a.y with object 
a=cse()                                    #but we can call x as a.x or cse.x
a.qwer() 
print(cse.x,a.y)