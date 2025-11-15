K, N = map(int, input().split())

# Please write your code here.
lst=[]
ans=[]

def choose(depth):
    if depth==N+1:
        ans.append(lst.copy())
        return

    for select in range(1,K+1):
        lst.append(select)
        choose(depth+1)
        lst.pop()

choose(1)
for per in ans:
    print(*per)