n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# k~k+m-1 까지 검사
height=n
location=0
for col in range(k,k+m):
    for row in range(n):
        if grid[row][col-1]==1:
            height=min(height,row)


for col in range(n):
    if grid[height-1][col]==0:
        grid[height-1][col]=1

for row in grid:
    print(*row)