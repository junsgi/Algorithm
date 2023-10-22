# https://www.acmicpc.net/problem/16118
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().strip().split())
    graph[s].append([e, c])
    graph[e].append([s, c])

wolf = [[float("inf")] * (n + 1) for _ in range(2)]
fox = [float("inf")] * (n + 1)
fox[1] = wolf[1][1] = 0
heap = []
heappush(heap, (0, -1, 1))
heappush(heap, (0, 1, 1))
while heap:
    cost, status, node  = heappop(heap)
    if status == -1 and fox[node] < cost: continue
    if status >= 0 and wolf[status][node] < cost: continue
    for nx, tc in graph[node]:
        if status == -1: # 여우면
            if fox[nx] <= tc + cost: continue
            fox[nx] = tc + cost
            heappush(heap, (tc + cost, status, nx))
        elif status == 1: # 빠른 늑대라면
            if wolf[0][nx] <= cost + tc / 2: continue
            wolf[0][nx] =  cost + tc / 2 
            heappush(heap, (cost + tc / 2, 0, nx))
        else: # 느린 늑대라면
            if wolf[1][nx] <= cost + tc * 2: continue
            wolf[1][nx] = cost + tc * 2
            heappush(heap, (cost + tc * 2, 1, nx))
ans = 0
for i in range(1, n + 1):
    if fox[i] < min(wolf[1][i], wolf[0][i]):
        ans += 1
print(ans)