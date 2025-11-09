n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer=0

for row in range(n): #행별로 행복 수열 찾기
    lst=[]
    count=1
    max_count=0
    for col in range(n):
        if lst and grid[row][col]==lst[-1]:
            count+=1

        if lst and grid[row][col]!=lst[-1]:
            max_count=max(max_count,count)
            count=1

        lst.append(grid[row][col])

    count=max(max_count,count)
    
    if count>=m:
        answer+=1


for col in range(n): #열별로 행복 수열 찾기
    lst=[]
    count=1
    max_count=0
    for row in range(n):
        if lst and grid[row][col]==lst[-1]:
            count+=1

        if lst and grid[row][col]!=lst[-1]:
            max_count=max(max_count,count)
            count=1

        lst.append(grid[row][col])
    
    count=max(max_count,count)

    if count>=m:
        answer+=1
    
    
    

print(answer)

