n = int(input())

# Please write your code here.
lst=[]
ans=[]
def choose():
    if len(lst)==n:
        ans.append(lst.copy())
        return
    if len(lst)>n:
        return

    for i in range(1,4+1):
        for _ in range(i):
            lst.append(i)
        choose()
        for _ in range(i):
            lst.pop()

choose()
print(len(ans))
