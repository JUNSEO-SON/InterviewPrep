n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
p=grid[r-1][c-1]
ans=[[0 for _ in range(n)] for _ in range(n)]

#폭탄 터트리기
for i in range(n):
    if c-1-p<i<c-1+p:
        grid[r-1][i]=0
    
    if r-1-p<i<r-1+p:
        grid[i][c-1]=0

for col in range(n):
    temp=[]
    for row in range(n):
        if grid[row][col]!=0:
            temp.append(grid[row][col])
    
    for i in range(n):
        if temp:
            ans[n-1-i][col]=temp.pop()



for a in ans:
    print(*a)