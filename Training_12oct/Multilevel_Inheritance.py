class cse:
    def fun1(self):
        print("Fun1")
    def fun2(s):
        print("Fun2")
class two(cse):
    def fun3(self):
        print("Fun3")
    def fun4(s):
        print("4")
class three(two):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun5()
b.fun3()
b.fun1()