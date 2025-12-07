
n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
lst=[]
ans=[]
def choose(start):
    if len(lst)==m:
        ans.append(lst.copy())
        return
    
    for i in range(start,n):
        lst.append(A[i])
        choose(i+1)
        lst.pop()

choose(0)
answer=0
for a in ans:
    temp=0
    for b in a:
        temp=b^temp
    answer=max(temp,answer)

print(answer)


