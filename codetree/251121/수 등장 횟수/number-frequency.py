from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.

cnt=Counter(arr)

for num in nums:
    print(cnt[num],end=' ')