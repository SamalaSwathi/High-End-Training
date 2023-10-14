n=int(input())
si=0
li=n//2
floor=-1
def sqrt(n,si,li,floor):
    if n<=0:
        return 0
    if n==1:
        return 1
    if si<=li:
        mid=(si+li)//2
        sq=mid*mid
        if sq==n:
            return mid
        elif sq<n:
            floor=mid
            return sqrt(n,mid+1,li,floor)
        else:
            return sqrt(n,si,mid-1,floor)
    return floor
print(sqrt(n,si,li,floor))
