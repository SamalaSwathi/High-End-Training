def totalNQueens(n):
    col=[]
    pd=[]
    nd=[]
    board=[["."]*n for i in range(n)]
    ans=[]
    def backtrack(r):
        if r==n:
            l=["".join(i) for i in board]
            ans.append(l)
            return
        for c in range(n):
            if c in col or (r+c) in pd or (r-c) in nd:
                continue
            board[r][c]="Q"
            col.append(c)
            pd.append(r+c)
            nd.append(r-c)
            backtrack(r+1)
            board[r][c]="."
            col.remove(c)
            pd.remove(r+c)
            nd.remove(r-c)
    backtrack(0)
    return len(ans)
n=int(input())
print(totalNQueens(n))