from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.


def bfs(grid,y,x):
    visited=[[False for _ in range(n)] for _ in range(n)]
    q=deque()

    y_grid=y-1
    x_grid=x-1

    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    
    if grid[y_grid][x_grid]==0:
        q.append((y_grid,x_grid))
        grid[y_grid][x_grid]=2
        count=1
        while q:
            row,col=q.popleft()
            for i in range(4):
                new_row=row+dy[i]
                new_col=col+dx[i]
                if 0<=new_row<n and 0<=new_col<n:
                    if grid[new_row][new_col]==0:
                        q.append((new_row,new_col))
                        grid[new_row][new_col]=2
                        count+=1
    
        return count
    
    return 0

answer=0
for point in points:
    answer+=bfs(grid,point[0],point[1])

print(answer)