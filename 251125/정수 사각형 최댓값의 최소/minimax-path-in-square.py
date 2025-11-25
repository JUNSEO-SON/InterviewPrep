from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp=[[0 for _ in range(n)] for _ in range(n)]
for i in range(len(dp)):
    for j in range(len(dp)):
        if j==0:
            dp[i][j]=max(grid[i][j],dp[i-1][j])
        if i==0:
            dp[i][j]=max(grid[i][j],dp[i][j-1])
        else:
            continue

for i in range(1,len(dp)):
    for j in range(1,len(dp)):
        dp[i][j]=max(min(dp[i-1][j],dp[i][j-1]),grid[i][j])


print(dp[n-1][n-1])