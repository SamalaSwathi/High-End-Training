def solve(arr):
    p1 = 0
    p2 = len(arr)-1
    while p1<p2:
        sum = arr[p1] + arr[p2]
        if sum == target:
            return (arr[p1], arr[p2])
        elif sum < target:
            p1 += 1
        else:
            p2 -= 1
    return False
    
arr = [2,3,4,5,6]
target = 17
result = solve(arr)
print(result)