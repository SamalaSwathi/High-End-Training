#Recursion demo 2
# To implement recursion
def cse(x):
    if(x==0):
        return 0
    print(x)
    print(cse(x-1))
    print(x)
cse(4)