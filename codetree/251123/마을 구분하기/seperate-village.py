n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
sizes=[]
# Please write your code here.
def dfs(grid,y,x):
    size=1
    grid[y][x]=2

    n=len(grid)
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    for i in range(4):
        if 0<=y+dy[i]<n and 0<=x+dx[i]<n:
            ny=y+dy[i]
            nx=x+dx[i]
            if grid[ny][nx]==1:
                size+=dfs(grid,ny,nx)
    
    return size
count=0
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            sizes.append(dfs(grid,i,j))
            count+=1

sizes.sort()

print(count)
print(*sizes,sep='\n')