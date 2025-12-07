n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d={}
for point in points:
    x=point[0]
    y=point[1]

    d[x]=min(d.get(x,float('inf')),y)

print(sum(d.values()))