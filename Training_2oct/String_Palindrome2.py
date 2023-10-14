s=input()
i=0
j=len(s)-1
while i<=j:
    if(s[i]!=s[j]):                            
        print("No")
        break
    i=i+1
    j=j-1
else:
    print("Yes")