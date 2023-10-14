#pattern-1
#logic-1
a=int(input())
for i in range(a):
    for j in range(i+1):
        print("*",end='')
    print()
    
#logic-2
a=int(input())
for i in range(a):
    print("* "* (i+1))
 
