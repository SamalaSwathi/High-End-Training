#Mergesorting: for the sorted two arrays i.e.,left and right.
'''def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergesort(left)
        right=mergesort(right)
        print(left,right)
        l=merge(left,right)
        #print(mergel)
        return mergel
    return l
def merge(left,right):
    res=[]
    i=j=k=0   #left=right=res=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
l=[3,9,3,1,0]
print(mergesort(l))'''


#without the merge function
def mergesort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergesort(left,inversion)
        ri=mergesort(right,inversion)
        i=j=k=0         #left=right=res=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
                inversion+=len(left)-i
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
        return li+ri+inversion
    return 0
l=[22, 54, 52, 417, ]
print("Inversion count:",mergesort(l,0))
print(l)