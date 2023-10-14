l=[]
n=int(input())
for i in range(n):
    e=int(input())
    l.append(e)
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(*l,sep="->")