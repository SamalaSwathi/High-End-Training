l= [int(l) for l in input().split(",")]
r=max(l)+1
count=[0 for i in range(r)]
for i in range (len(l)):
    count[l[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(l)
for i in range(len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(*res,sep="->")