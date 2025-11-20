n = int(input())

# Please write your code here.
dp=[0,1,2]

for i in range(3,1000+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n]%10007)