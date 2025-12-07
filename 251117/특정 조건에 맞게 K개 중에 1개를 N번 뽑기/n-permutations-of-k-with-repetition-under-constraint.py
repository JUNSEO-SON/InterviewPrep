K, N = map(int, input().split())

# Please write your code here.
ans=[]
lst=[]

def choose(count):
    if len(lst)==N:
        ans.append(lst.copy())
        return

    for i in range(1,K+1):
        if lst and lst[-1]==i:
            new_count=count+1
        else:
            new_count=1
        
        if new_count<3:
            lst.append(i)
            choose(new_count)
            lst.pop()
        

choose(1)
for a in ans:
    print(*a)



