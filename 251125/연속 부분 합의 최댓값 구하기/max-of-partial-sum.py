n = int(input())
arr = list(map(int, input().split()))
dp=[0 for _ in range(len(arr))]
dp[0]=arr[0]
# Please write your code here.
for i in range(1,len(arr)):
    dp[i]=max(dp[i-1]+arr[i],arr[i])

print(max(dp))