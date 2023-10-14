#creating a constructer with parameters
class cse:
    def _init_(self,b):
        print("i am default constructer",b)
        print(b)
    def fun(self):
        print("i am a method in class cse")
obj=cse(2)  
obj.fun()
obj._init_(5)
