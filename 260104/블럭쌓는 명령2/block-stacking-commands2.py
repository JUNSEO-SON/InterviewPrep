n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

blocks=[0 for _ in range(n+1)]
for start,end in commands:
    for i in range(start,end+1):
        blocks[i]+=1

print(max(blocks))