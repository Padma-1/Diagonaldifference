def diagonalDifference(arr):
    leftsum=0
    rightsum=0
    c=0
    d=n-1
    for i in range(len(arr)):
        leftsum+=(arr[c][c])
        rightsum+=(arr[c][d])
        c+=1
        d-=1
    return abs(leftsum-rightsum)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(str(result))
"""
3
1 2 3
4 5 6
9 8 9 
output:2-->|(1+5+9)-(3+5+9)|

