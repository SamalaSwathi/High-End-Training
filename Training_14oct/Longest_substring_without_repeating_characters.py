#leetcode:3
"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def lengthOfLongestSubstring(s):
    l,longestSubString=0,0
    sw=set()
    for r in range(len(s)):
        while s[r] in sw:
            sw.remove(s[l])
            l+=1
        sw.add(s[r])
        longestSubString=max(longestSubString,(r-l+1))
    return longestSubString
s=input()
print(lengthOfLongestSubstring(s))