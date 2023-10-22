# https://www.acmicpc.net/problem/1753
from heapq import heappush, heappop
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    st, ed, c = map(int, input().split())
    graph[st].append((ed, c))
heap = []
limit = [float("inf")] * (n + 1)
heappush(heap, (0, start))
limit[start] = 0
while heap:
    y, x = heappop(heap)
    if limit[x] < y : continue
    for node, cost in graph[x]:
        if limit[node] <= cost + y: continue
        limit[node] = cost + y
        heappush(heap, (cost + y, node))
for i in range(1, n + 1):
    if limit[i] == float("inf"): print("INF")
    else:print(limit[i])