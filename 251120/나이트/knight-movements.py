from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())


# Please write your code here.

grid=[[0 for _ in range(n+1)] for _ in range(n+1)]

def knight_bfs(grid,r1,c1,r2,c2):
    dy=[-1,-2,-2,-1,1,2,2,1]
    dx=[-2,-1,1,2,2,1,-1,-2]

    q=deque()

    q.append((r1,c1,1))
    grid[r1][c1]=1

    while q:
        r,c,count=q.popleft()
        for i in range(8):
            n_r,n_c=r+dy[i],c+dx[i]

            if 1<=n_r<=n and 1<=n_c<=n:
                if grid[n_r][n_c]==0:
                    q.append((n_r,n_c,count+1))
                    grid[n_r][n_c]=1
                    if n_r==r2 and n_c==c2:
                        return count

ans=knight_bfs(grid,r1,c1,r2,c2)

if grid[r2][c2]==1:
    print(ans)
else:
    print(-1)