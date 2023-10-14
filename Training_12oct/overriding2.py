class cse:
    def fun1(self):
        print("Fun1")
class two(cse):
    def fun1(self):
        print("Fun3")
class three(two):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun1()