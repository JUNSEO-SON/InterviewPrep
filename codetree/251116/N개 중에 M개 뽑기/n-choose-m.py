N, M = map(int, input().split())

# Please write your code here.
ans=[]
lst=[]
def choose(depth):
    if depth==M+1:
        ans.append(lst.copy())
        return

    if lst:
        start=max(depth,lst[-1])
    else:
        start=depth
        
    for i in range(start,N+1):
        if i not in lst:
            lst.append(i)
            choose(depth+1)
            lst.pop()

choose(1)
for com in ans:
    print(*com)


