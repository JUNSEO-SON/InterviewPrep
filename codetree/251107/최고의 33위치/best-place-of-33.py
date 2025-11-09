n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans=0

def gridsum(dx,dy):
    total=0
    for row in range(dx,dx+3):
        for col in range(dy,dy+3):
            if grid[row][col]==1:
                total+=1

    return total

for dx in range(n-2):
    for dy in range(n-2):
        curr_sum=gridsum(dx,dy)
        ans=max(curr_sum,ans)

print(ans)
