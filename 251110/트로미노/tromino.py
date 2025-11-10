n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def square(grid,row,col):
    total=grid[row][col]
    dy=[1,0,1]
    dx=[0,1,1]
    for i in range(3):
        total+=grid[row+dy[i]][col+dx[i]]

    return max(total-grid[row][col],total-grid[row+1][col],total-grid[row+1][col+1],total-grid[row][col+1])

def hor(grid,row,col):
    total=grid[row][col]
    total+=grid[row][col+1]+grid[row][col+2]
    return total

def ver(grid,row,col):
    total=grid[row][col]
    total+=grid[row+1][col]+grid[row+2][col]
    return total

ans=[]

for i in range(n):
    for j in range(m-2):
        ans.append(hor(grid,i,j))

for i in range(n-2):
    for j in range(m):
        ans.append(ver(grid,i,j))

for i in range(n-1):
    for j in range(m-1):
        ans.append(square(grid,i,j))

print(max(ans))


