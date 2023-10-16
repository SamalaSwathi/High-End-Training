#leetcode: 189
"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rotate(nums,k):
    for i in range(k):
        a=nums.pop()
        nums.insert(0,a)
    return nums
nums=list(map(int,input().split()))
k=int(input())
print(rotate(nums,k))