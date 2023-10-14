def isValid(s):
    open=['{','[','(']
    closed=['}',']',')']
    braces={'}':'{',']':'[',')':'('}
    stack=[]
    for char in s:
        if char in open:
            stack.append(char)
        elif char in closed:
            if not stack or braces[char]!=stack.pop():
                return False
    return len(stack)==0
n=input()
print(isValid(n))