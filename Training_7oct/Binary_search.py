def bs(l,key):
    si=0
    li=len(l)-1
    while(si<=li):
        mid=(si+li)//2
        if l[mid]==key:
            print(l[mid])
            break
        elif l[mid]<key:
            si=mid+1
        else:
            li=mid-1
l=list(map(int,input().split()))
key=int(input())
bs(l,key)