# Recursion demo 1
#To print numbers in increasing and decresing order using recursion
def cse(x):
    if(x==0):
        return 0
    print(x)
    cse(x-1)
    print(x)
cse(4)