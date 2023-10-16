#leetcode-33
"""Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""


def search(nums,target):
    si=0
    li=len(nums)-1
    while si<=li:
        mid=(si+li)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>=nums[si]:
            if target>=nums[si] and target<=nums[mid]:
                li=mid-1
            else:
                si=mid+1
        else:
            if target>nums[mid] and target<=nums[li]:
                si=mid+1
            else:
                li=mid-1
     return -1
    
nums=list(map(int,input().split()))
target=int(input())
print(search(nums,target))
