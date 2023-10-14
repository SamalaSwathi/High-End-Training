class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=[]
        posidiag=[]
        negdiag=[]
        board=[["."]*n for i in range(n)]
        ans=[]
        def backtracking(r):
            if r==n:
                l=["".join(i) for i in board]
                ans.append(l)
                return
            for c in range(n): 
                if c in col or (r+c) in posidiag or (r-c) is negdiag:
                    continue
                board[r][c]="Q"
                col.append(c)
                posidiag.append(r+c)
                negdiag.append(r-c)
                backtracking(r+1)
                board[r][c]='.'
                col.remove(c)
                posidiag.remove(r+c)
                negdiag.remove(r-c)
        backtracking(0)
        return ans