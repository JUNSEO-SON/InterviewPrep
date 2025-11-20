n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

locations = [1 for _ in range(k+1)]
locations[0]=-1
ans = 0

def find_max_score(turn_cnt):
    global ans
    
    if turn_cnt == n:
        score=0
        for location in locations:
            if location>=m:
                score+=1
        ans = max(ans, score)
        return 

    move = nums[turn_cnt]
    
    for i in range(1,k+1):
        if locations[i] >= m:
            continue
        locations[i] += move
        find_max_score(turn_cnt + 1)
        locations[i] -= move

# 실행
find_max_score(0)
print(ans)