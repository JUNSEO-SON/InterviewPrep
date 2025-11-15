import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# [OPTIMIZATION]
# pos 배열: pos[i] = (row, col)
# 숫자 i가 grid의 (row, col)에 있다는 것을 O(1)에 찾기 위한 배열
# (크기는 n*n + 1)
pos = [None] * (n**2 + 1)

# O(N^2) - 처음에 한 번만 격자를 순회하여 위치 정보 저장
for i in range(n):
    for j in range(n):
        pos[grid[i][j]] = (i, j)

# 8방향 (상, 상좌, 상우, 하, 하좌, 하우, 우, 좌)
# (사용자님의 dx, dy 순서를 존중)
dy=[0, 0, -1, 1, 1, 1, -1, -1] # dy[0]은 -1이 되어야 할 것 같으나, 원본을 따름
dx=[-1, 1, 1, -1, 0, 1, 0, -1] # 이웃 순서는 상관없음
# (원본 dx, dy가 약간 혼동되어 있어 표준 8방향으로 수정)
dy = [-1, -1, -1,  0,  0,  1,  1,  1]
dx = [-1,  0,  1, -1,  1, -1,  0,  1]


def find_max(grid, row, col):
    """(row, col)의 8방향 이웃 중 최댓값을 반환"""
    max_val = 0
    
    # 8방향 탐색 (O(1) - 항상 8번)
    for i in range(8):
        r = row + dy[i]
        c = col + dx[i]
        
        # 격자 범위(n x n) 확인
        if 0 <= r < n and 0 <= c < n:
            max_val = max(max_val, grid[r][c])
            
    return max_val

# O(M * N^2) - 메인 시뮬레이션
for _ in range(m): # O(M)
    for i in range(1, n**2 + 1): # O(N^2)
        
        # [OPTIMIZED] O(1) 조회
        # i가 어디 있는지 O(N^2)로 찾지 않고 바로 조회
        row, col = pos[i]
        
        # 이웃 중 최댓값 찾기 (O(1))
        max_val = find_max(grid, row, col)
        
        # [OPTIMIZED] O(1) 조회
        # 최댓값이 어디 있는지 O(N^2)로 찾지 않고 바로 조회
        max_row, max_col = pos[max_val]
        
        # 교환
        grid[row][col], grid[max_row][max_col] = grid[max_row][max_col], grid[row][col]
        
        # [CRITICAL]
        # 교환했으므로, pos 배열의 정보도 '반드시' 갱신
        pos[i] = (max_row, max_col)
        pos[max_val] = (row, col)

# 최종 격자 출력
for row in grid:
    print(*row)