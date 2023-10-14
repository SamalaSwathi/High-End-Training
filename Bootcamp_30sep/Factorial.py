#Factorial using recursion
def cse(x):       
    if(x==0):
        return 1
    return x*cse(x-1)
print(cse(5))