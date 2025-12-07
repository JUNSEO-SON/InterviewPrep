n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=grid[0][0]
ans=0
for col in range(n):
    for row in range(n):
        if col==0 and row>=1:
            dp[row][col]=dp[row-1][col]+grid[row][col]

        if row==0 and col>=1:
            dp[row][col]=dp[row][col-1]+grid[row][col]
#  -----------------------------------------------------------

        if row>=1 and col>=1:
            dp[row][col]=max(dp[row-1][col]+grid[row][col],dp[row][col-1]+grid[row][col])


print(max(dp[n-1]))