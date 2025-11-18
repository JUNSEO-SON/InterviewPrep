from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.

def bfs(grid,row,col):
    visited=[[False for _ in range(m)] for _ in range(n)]
    dq=deque()
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    dq.append((row,col))
    
    while dq:
        row,col=dq.popleft()
        visited[row][col]=True
        for i in range(4):
            move_row=row+dy[i]
            move_col=col+dx[i]

            if 0<=move_col<m and 0<=move_row<n:
                if grid[move_row][move_col]==1 and visited[move_row][move_col]==False:
                    dq.append((move_row,move_col))

    return visited[n-1][m-1]

print(int(bfs(a,0,0)))

