class cse:
    def fun1(self):
        print("Fun-father")
    def fun2(self):
        print("Fun2")
class two:
    def fun1(self):
        print("Fun-mother")
    def fun3(self):
        print("Fun3")
class three(cse,two):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun1()
b.fun2()
b.fun3()