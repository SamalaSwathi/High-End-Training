W=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
print(l)
maxpr=0
for weight,profit in l:
    if weight<=W:
        maxpr+=profit
        W-=weight
    else:
        maxpr+=W*(profit/weight)
        break
print(maxpr)