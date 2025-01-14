from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = 0
    heap = []
    for i in enemy:
        heappush(heap, i)
        if len(heap) > k:
            n -= heappop(heap)
            if n < 0:
                break
        answer += 1
    return answer