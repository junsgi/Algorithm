# https://www.acmicpc.net/problem/16118
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def FOX():
    tCost = 0
    heappush(heap, (0, 1))
    fox = [INF] * (n + 1)
    fox[1] = 0
    while heap:
        cst, nd = heappop(heap)
        if fox[nd] < cst : continue
        for nx, c in graph[nd]:
            tCost = c + cst
            if fox[nx] > tCost:
                fox[nx] = tCost
                heappush(heap, (tCost, nx))
    return fox

def WOLF():
    # 0 느린상태
    # 1 빠른상태
    tCost = 0
    wolf = [[INF] * (n + 1) for _ in range(2)]
    heappush(heap, (0, 1, 1))
    wolf[0][1] = 0
    while heap:
        cst, nd, status = heappop(heap)
        if wolf[status][nd] < cst: continue 
        for nx, c in graph[nd]:
            if status:
                tCost = (c >> 1) + cst
            else:
                tCost = (c << 1) + cst
            if wolf[not status][nx] > tCost: # 다음 상태로 도착할 때 비용이 덜 든다면
                wolf[not status][nx] = tCost
                heappush(heap, (tCost, nx, not status))
    return wolf
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c * 2]) # 나누기 2를 하면서 생긴 소수 계산 해결
    graph[e].append([s, c * 2])
INF = 1e12
heap = []
fox = FOX()
wolf = WOLF()
ans = 0
for i in range(1, n + 1):
    if fox[i] < min(wolf[1][i], wolf[0][i]):
        ans += 1
print(ans)