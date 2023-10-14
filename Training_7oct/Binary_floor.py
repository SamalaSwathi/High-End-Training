def bs_floor(l,key,si,li,floor):
    if(si<=li):
        mid=(si+li)//2
        if l[mid]==key:
            return l[mid]
        if l[mid]<key:
            floor=l[mid]
            return bs_floor(l,key,mid+1,li,floor)
        else:
            return bs_floor(l,key,si,mid-1,floor)
    return floor
l=list(map(int,input().split()))
key=int(input())
print(bs_floor(l,key,0,len(l)-1,-1))