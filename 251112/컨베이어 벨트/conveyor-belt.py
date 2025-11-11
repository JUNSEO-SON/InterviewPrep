n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# 123651 -> 112365
lst=u+d


def pusher(lst):
    temp=lst.pop()
    lst.insert(0,temp)
    return lst

for _ in range(t):
    lst=pusher(lst)

print(*lst[:n])
print(*lst[n:])