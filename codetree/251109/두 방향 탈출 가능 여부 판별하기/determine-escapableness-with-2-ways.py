n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dy=[1,0] #아래만 이동가능
dx=[0,1] #오른쪽만 이동가능

def dfs(grid,y,x):
    grid[y][x]=2
    for i in range(2):
        if 0<=y+dy[i]<n and 0<=x+dx[i]<m:
            if grid[y+dy[i]][x+dx[i]]==1:
               dfs(grid,y+dy[i],x+dx[i]) 

dfs(grid,0,0)

# print(*grid,sep='\n')
if grid[n-1][m-1]==2:
    print(1)
else:
    print(0)

