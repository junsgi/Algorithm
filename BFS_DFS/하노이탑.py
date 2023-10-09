# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    answer = []
    
    def hanoi(depth, current, target):
        if depth == 0: return
        # depth - 1 원판은 현재 위치에서 다음위치로
        hanoi(depth - 1, current, 6 - target - current)
        answer.append([current, target])
        
        # depth - 1 원판은 목적지(6 - target - current)에 위치중이기 때문에
        # depth - 1 원판을 현재 원판 위에다 두어야 함
        hanoi(depth - 1, 6 - target - current, target)
        
    # n번 원판은 1번 기둥에서 3번 기둥으로
    hanoi(n, 1, 3)
    return answer