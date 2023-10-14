#Class and objects demo-1
class cse:
    def qwer(self):
        print("Hi")         #If it contains self then it is a static method
a=cse()
a.qwer()                 #If the variable is not linked to the object then it is static variable
cse.qwer(20)