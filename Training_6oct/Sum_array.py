#sum of all the elements in an array using binary search
def sum(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return sum(l,si,mid)+sum(l,mid+1,li)
l=[2,3,4,5]
print(sum(l,0,len(l)-1))


