def generateParenthesis(n):
    l=[]
    res=[]
    def backtrack(opencount=0,closecount=0):
        if(opencount==closecount==n):
            res.append("".join(l))
        if opencount<n:
            l.append('(')
            backtrack(opencount+1,closecount)
            l.pop()
        if closecount<opencount:
            l.append(')')
            backtrack(opencount,closecount+1)
            l.pop()
        return res
    return backtrack()
n=int(input())
generateParanthesis(n)
print(l)