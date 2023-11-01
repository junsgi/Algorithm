# https://www.acmicpc.net/problem/1238
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
heap = []
N, M, TARGET = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
answer = 0
def dijkstra(x):
    global TARGET
    heappush(heap, [0, x, True])
    go = [1e12] * (N + 1)
    back = [1e12] * (N + 1)
    go[x] = 0
    while heap:
        cost, node, status = heappop(heap)
        if status and go[node] < cost: continue
        if not status and back[node] < cost: continue

        for ed, tc in graph[node]:
            newCost = tc + cost
            if status and go[ed] > newCost: 
                if ed == TARGET: # 파티 장소에 도착했다면
                    back[ed] = newCost
                    heappush(heap, [newCost, ed, not status])
                else:
                    go[ed] = newCost
                    heappush(heap, [newCost, ed, status])
            
            if not status and back[ed] > newCost:
                back[ed] = newCost
                heappush(heap, [newCost, ed, status])
    return back[x]
for i in range(1, N + 1):
    if i == TARGET:continue
    if graph[i]:
        answer = max(answer, dijkstra(i))
print(answer)