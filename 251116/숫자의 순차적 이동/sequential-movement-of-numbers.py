n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def find_idx(grid,value):

    l=len(grid)
    for row in range(l):
        for col in range(l):
            if grid[row][col]==value:
                return row,col

def find_max(grid,row,col):

    dx=[-1,-1,-1,1,1,1,0,0]
    dy=[0,-1,1,0,-1,1,1,-1]
    l=len(grid)
    max_val=0
    for i in range(8):
        r=row+dy[i]
        c=col+dx[i]
        if 0<=r<l and 0<=c<l:
            max_val=max(max_val,grid[r][c])
    
    return max_val
for _ in range(m):
    for i in range(1,n**2+1):
        row,col=find_idx(grid,i)
        max_val=find_max(grid,row,col)
        max_row,max_col=find_idx(grid,max_val)
        # print(f'{i}일때 최대값{max_val} {row}행{col}열과 {max_row}행{max_col}열을 교환')
        grid[row][col],grid[max_row][max_col]=grid[max_row][max_col],grid[row][col]

for row in grid:
    print(*row)