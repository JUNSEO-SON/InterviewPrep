n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
#  124593651

k=t%(3*n)
lst=l+r+d
for _ in range(k):
    lst=[lst[-1]]+lst[:len(lst)-1]

print(*lst[:3])
print(*lst[3:6])
print(*lst[6:9])