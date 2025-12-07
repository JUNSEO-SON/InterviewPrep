n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

locations = [1 for _ in range(k+1)]
locations[0] = -1 # 0번 인덱스 사용 안 함
ans = 0

# current_score: 현재까지 도착한 말의 개수를 인자로 받음
def find_max_score(turn_cnt, current_score):
    global ans
    
    # 1. 매 순간 최댓값 갱신 (루프 없이 O(1))
    ans = max(ans, current_score)

    if turn_cnt == n:
        return 

    move = nums[turn_cnt]
    
    for i in range(1, k+1):
        # 이미 도착한 말은 선택하지 않음 (점수 변동 없음)
        if locations[i] >= m:
            continue
            
        # [상태 변경]
        locations[i] += move
        
        # [점수 판별] 방금 이동으로 인해 도착했는지 확인
        next_score = current_score
        if locations[i] >= m:
            next_score += 1
            
        # [다음 단계] 갱신된 점수를 넘겨줌
        find_max_score(turn_cnt + 1, next_score)
        
        # [상태 복구] 위치는 원상복구해야 함 (점수는 인자라 복구 불필요)
        locations[i] -= move

# 시작: 0턴, 0점
find_max_score(0, 0)
print(ans)