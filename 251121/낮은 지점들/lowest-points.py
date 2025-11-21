n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d={}
for point in points:
    x=point[0]
    y=point[1]
    if x in d:
        d[x]=min(d[x],y)
        
    else:
        d[x]=y

print(sum(d.values()))