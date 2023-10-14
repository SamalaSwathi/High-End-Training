l=list(map(int,input().split()))
flag=False
n=len(l)
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
        if flag==False:
            break
        flag=False
print(*l)