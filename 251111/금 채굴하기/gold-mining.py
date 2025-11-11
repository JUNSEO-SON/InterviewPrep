n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def distance(grid,y,x,k):
    gold=0
    count=0
    for row in range(n):
        for col in range(n):
            if abs(y-row)+abs(x-col)<=k:
                count+=1
                if grid[row][col]==1:
                    gold+=1
    return count,gold

max_gold=0
for i in range(n):
    for j in range(n):
        for k in range(1,n+1):
            count,gold=distance(grid,i,j,k)
            if k**2+(k+1)**2 <= m*gold:
                max_gold=max(gold,max_gold)

print(max_gold)