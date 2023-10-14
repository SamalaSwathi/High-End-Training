def bs_ceil(l,key,si,li,ceil):
    if(si<=li):
        mid=(si+li)//2
        if l[mid]==key:
            return l[mid]
        if l[mid]<key:
            return bs_ceil(l,key,mid+1,li,ceil)
        else:
            ceil=l[mid]
            return bs_ceil(l,key,si,mid-1,ceil)
    return ceil
l=list(map(int,input().split()))
key=int(input())
print(bs_ceil(l,key,0,len(l)-1,-1))