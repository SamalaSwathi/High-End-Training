def sqrt_binary(number,epsilon=1e-8):
    if number<0:
        raise ValueError("Cannot compute th square root of the number")
    if number<1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_squared=mid*mid
        if mid_squared<number:
            left=mid
        else:
            right=mid
    return(left+right)/2
number=int(input())
result=sqrt_binary(number)
print(result)