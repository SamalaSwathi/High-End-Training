n=input()
def fun(n):
    for i in range(0,len(n)//2):                    
        if(n[i]!=n[len(n)-i-1]):
            return 0
    return 1
print(fun(n))
