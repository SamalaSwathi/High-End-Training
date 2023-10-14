l=list(map(int,input().split()))
target=int(input())
flag=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==target:
                flag=1
                break
if flag==1:
    print("Found")
else:
    print("Not Found")
print(l)