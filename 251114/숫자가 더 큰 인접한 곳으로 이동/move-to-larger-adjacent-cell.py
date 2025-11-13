n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dx=[0,0,-1,1]
dy=[-1,1,0,0]

ans=[]
def move(grid,y,x):
    ans.append(grid[y][x])
    for i in range(4):
        new_y=y+dy[i]
        new_x=x+dx[i]
        if 0<=new_y<n and 0<=new_x<n:
            if grid[new_y][new_x]>grid[y][x]:
                break
            
    if grid[new_y][new_x]>grid[y][x]:
        move(grid,new_y,new_x)
    
move(a,r,c)
print(*ans)
        

