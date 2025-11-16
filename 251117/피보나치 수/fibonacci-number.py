N = int(input())

# Please write your code here.
dp=[0,1,1,2,3]

for i in range(5,46):
    dp.append(dp[i-1]+dp[i-2])

print(dp[N])
