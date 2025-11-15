n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

count = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(len(r)):
    count[r[i]][c[i]]=1


# Please write your code here.
def find_location(count):
    r=[]
    c=[]
    for i in range(n+1):
        for j in range(n+1):
            if count[i][j]==1:
                r.append(i)
                c.append(j)
            else:
                count[i][j]=0

    return r,c

def move(grid,count):
    r,c=find_location(count)
    next_count=[[0 for _ in range(n+1)] for _ in range(n+1)]

    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    for i in range(len(r)): #구슬 하나씩 꺼내
        row=r[i]-1
        col=c[i]-1
        maxnum=-1
        for j in range(4): #최대값 찾기
            if 0<=row+dy[j]<n and 0<=col+dx[j]<n: #index 유효성 검사
                maxnum=max(maxnum,grid[row+dy[j]][col+dx[j]])

        for j in range(4):
            if 0<=row+dy[j]<n and 0<=col+dx[j]<n:
                if grid[row+dy[j]][col+dx[j]]==maxnum:
                    if next_count[row+dy[j]+1][col+dx[j]+1]:
                        next_count[row+dy[j]+1][col+dx[j]+1]+=1
                    else:
                        next_count[row+dy[j]+1][col+dx[j]+1]=1

    return next_count
for _ in range(t):
    count=move(a,count)

ans=0
for i in range(n+1):
    for j in range(n+1):
        if count[i][j]==1:
            ans+=1

print(ans)
