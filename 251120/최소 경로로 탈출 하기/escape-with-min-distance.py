from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def bfs(grid):

    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    q=deque()

    q.append((0,0,0))
    grid[0][0]=2
    while q:
        r,c,d=q.popleft()

        d+=1
        for i in range(4):
            n_r=r+dr[i]
            n_c=c+dc[i]

            if 0<=n_r<n and 0<=n_c<m:
                if grid[n_r][n_c]==1:
                    grid[n_r][n_c]=2
                    q.append((n_r,n_c,d))
                    if n_r==n-1 and n_c==m-1:
                        return d


d=bfs(a)

if a[n-1][m-1]==2:
    print(d)
else:
    print(-1)