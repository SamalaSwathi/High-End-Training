def subset(nums,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if backtrack(start+1,sum+nums[start]):
            subset.append(nums[start])
            return True
        return backtrack(start+1,sum)
    subset=[]
    if backtrack(0,0):
        return True
    else:
        return False,[]
nums=list(map(int,input().split()))
target_sum=int(input())

r=subset(nums,target_sum)
print(r)
'''

bool,subset=subset(nums,target_sum)
if bool:
    print("True")
else:
    print("False")
    '''