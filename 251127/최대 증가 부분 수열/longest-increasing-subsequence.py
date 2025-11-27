n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
lis=[1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if m[j]<m[i]:
            lis[i]=max(lis[i],lis[j]+1)


print(max(lis))