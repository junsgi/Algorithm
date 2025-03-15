# https://school.programmers.co.kr/learn/courses/30/lessons/42628
from heapq import heappush, heappop
from collections import deque
def solution(operations): 
    heap = []
    que = deque()

    for c in operations:
        comm, value = c.split()
        if comm == 'I': # 숫자 입력
            heappush(heap, int(value))
        else:
            que.clear()
            while heap: # 큐엔 정렬된 값이 들어감
                que.append(heappop(heap))

            if value == '-1' and que:
                que.popleft()
            elif value == '1' and que:
                que.pop()

            while que: # 다시 heap에 삽입
                heappush(heap, que.popleft())
    que.clear()
    while heap:
        que.append(heappop(heap))
        
    if que:
        return [que[-1], que[0]]
    else:
        return [0, 0]