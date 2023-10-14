#accessing object value
class cse:
    def _init_(self,b):
        self.b=b
    def fun(self):
        print("i am a method in class cse",self.b)
obj=cse(2)  
obj.fun()
