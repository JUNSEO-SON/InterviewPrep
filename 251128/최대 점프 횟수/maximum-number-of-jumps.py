n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


dp = [-1] * n
dp[0] = 0

for i in range(n):
    if dp[i] == -1:
        continue
    
    for j in range(1, arr[i] + 1):
        if i + j < n:
            dp[i + j] = max(dp[i + j], dp[i] + 1)

print(max(dp))