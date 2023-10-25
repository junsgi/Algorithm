# https://www.acmicpc.net/problem/16118
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
heap = []
for _ in range(m):
    s, e, c = map(int, input().strip().split())
    graph[s].append([e, c * 2]) # 나누기 2를 하면서 생긴 부동 소수점 문제 해결
    graph[e].append([s, c * 2])

wolf = [[1e12] * (n + 1) for _ in range(2)]
fox = [1e12] * (n + 1)

heappush(heap, (0, 1))
fox[1] = 0
while heap:
    cst, nd = heappop(heap)
    if fox[nd] < cst : continue
    for nx, c in graph[nd]:
        if fox[nx] <= c + cst: continue
        fox[nx] = c + cst
        heappush(heap, (c + cst, nx))

# 0 느린상태
# 1 빠른상태
heappush(heap, (0, 1, 1))
wolf[0][1] = 0
while heap:
    cst, nd, status = heappop(heap)
    if status and wolf[0][nd] < cst: continue
    if not status and wolf[1][nd] < cst : continue

    for nx, c in graph[nd]:
        if status and wolf[0][nx] >= c / 2 + cst:
            wolf[0][nx] = c / 2 + cst
            heappush(heap, (c / 2 + cst, nx, 0))
        
        if not status and wolf[1][nx] >= c * 2 + cst:
            wolf[1][nx] = c * 2 + cst
            heappush(heap, (c * 2 + cst, nx, 1))
ans = 0
for i in range(2, n + 1):
   # if wolf[1][i] == 1e12 or wolf[0][i] == 1e12: continue
    if fox[i] < min(wolf[1][i], wolf[0][i]):
        ans += 1
print(ans)
print(fox[1:])
print(wolf[0][1:])
print(wolf[1][1:])