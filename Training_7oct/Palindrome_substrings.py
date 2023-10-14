#To print all the palindrome substrings
def palin(s):
    n=len(s)
    def palin_rev(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    res=[]
    for i in range(len(s)):
        pal=palin_rev(i,i)
        if len(pal)>1:
            res.append(pal)
        pal2=palin_rev(i,i+1)
        if len(pal2)>1:
            res.append(pal2)
    return res
s=input()
print(palin(s))