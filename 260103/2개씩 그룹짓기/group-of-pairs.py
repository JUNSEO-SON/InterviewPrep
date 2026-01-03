n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

ans=0
size=len(nums)//2+1

for i in range(size):
    ans=max(ans,nums[i]+nums[-1-i])

print(ans)