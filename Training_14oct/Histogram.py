l=list(map(int,input().split()))
maxele=max(l)
for i in range(maxele,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()