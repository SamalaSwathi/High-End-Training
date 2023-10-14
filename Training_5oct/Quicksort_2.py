def func(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[i for i in arr if i<pivot]
    right=[i for i in arr if i>pivot]
    return func(left)+[pivot]+func(right)
l=list(map(int,input().split()))
a=func(l)
print(*a,sep="->")