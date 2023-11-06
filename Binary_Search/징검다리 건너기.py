# https://school.programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    answer = 0
    le = 1
    ri = max(stones) + 1
    mid = 0
    while le <= ri:
        mid = (le + ri) // 2
        cnt = 0
        for v in stones:
            if v - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                cnt = -1
                break
        if cnt == -1: # 떨어진 디딤돌이 k개 이상이면 이동할 수 있는 친구의 수를 줄인다
            answer = mid
            ri = mid - 1
        else: # 친구 모두가 이동했다면 친구의 수를 늘린다.
            le = mid + 1
    return answer