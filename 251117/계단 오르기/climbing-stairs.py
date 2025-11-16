n = int(input())

# Please write your code here.

dp=[0,0,1,1,1]
for i in range(6,1001):
    dp.append(dp[i-2]+dp[i-3])

print(dp[n]%10007)