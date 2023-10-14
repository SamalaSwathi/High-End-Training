#Leet code:42
"""Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped."""

def trap(height):
    res=0
    if not height:return True
    l=0
    r=len(height)-1
    maxl=height[l]
    maxr=height[r]
    while l<r:
        if maxl<maxr:
            l+=1
            maxl=max(maxl,height[l])
            res+=maxl-height[l]
        else:
            r-=1
            maxr=max(maxr,height[r])
            res+=maxr-height[r]
    return res
l=list(map(int,input().split()))
print(trap(l))