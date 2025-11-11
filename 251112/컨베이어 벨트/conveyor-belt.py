n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# 123651 -> 112365
lst=u+d


def pusher(lst):
    temp=lst.pop()
    lst=[temp]+lst[:] #2회연산
    return lst

for _ in range(t%(2*n)):
    lst=pusher(lst)

print(*lst[:n])
print(*lst[n:])