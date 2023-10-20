# https://www.acmicpc.net/problem/11000
import heapq
n = int(input())
arr = []
heap = []
answer = 0
for _ in range(n):
    st, ed = map(int, input().split())
    arr.append([st, ed])
arr.sort(key = lambda x : x[0])

for i in range(n):
    st, ed = arr[i]
    if not heap: 
        heapq.heappush(heap, ed)
        answer += 1
    else:
        # 현재 가장 빨리 끝나는 시간
        time = heapq.heappop(heap)

        if time > st: # 이전 회의가 아직 끝나지 않았으면 새로운 강의실 사용
            heapq.heappush(heap, time)
            answer += 1
        heapq.heappush(heap, ed)
print(answer)
