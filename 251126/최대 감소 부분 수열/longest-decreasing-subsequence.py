n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp=[0 for _ in range(n)]
dp[0]=1

for i in range(n):
    for j in range(i):
        if m[j]>m[i]:
            dp[i]=max(dp[j]+1,dp[i])



print(max(dp))