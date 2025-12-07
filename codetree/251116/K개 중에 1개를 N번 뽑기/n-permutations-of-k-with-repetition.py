K, N = map(int, input().split())

# Please write your code here.
lst=[]
ans=[]

def choose():
    if len(lst)==N:
        ans.append(lst.copy())
        return

    for i in range(1,K+1):
        lst.append(i) #i=1 [1] [1,1] 
        choose()
        lst.pop()

choose()

for a in ans:
    print(*a)
