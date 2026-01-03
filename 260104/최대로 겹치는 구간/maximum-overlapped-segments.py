n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lst=[0 for _ in range(201)]

for s,e in segments:
    s,e=s+100,e+100
    for i in range(s,e):
        lst[i]+=1
    
print(max(lst))