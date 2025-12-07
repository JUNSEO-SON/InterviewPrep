n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# k~k+m-1 까지 검사
height=n
# location=0
for col in range(k,k+m):
    for row in range(n):
        if grid[row][col-1]==1:
            if min(height,row)!=height:
                height=min(height,row)
                # location=col-1

target_height=height-1

#location부터 m개 -> 
for col in range(k-1,k-1+m):
    grid[target_height][col]=1


for row in grid:
    print(*row)