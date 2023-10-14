#Number pattern
#logic 1
a=int(input())
for i in range(a):
    print(str(i+1)*(i+1))
    
#Number pattern
#logic 2
a=int(input())
b=1
for i in range(1,a+1):
    print(b*i)
    b=(b*10)+1

#Number pattern
#logic 3
a=int(input())
for i in range(1,a+1):
    print(((10**i)//9)*i)
