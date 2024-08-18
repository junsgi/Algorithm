from collections import defaultdict
from heapq import heappush, heappop
n, e = map(int, input().split())
graph = defaultdict(list)
costs = [[0x7fffffff] * (n + 1) for _ in range(1 << 3)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
x1, x2 = map(int, input().split())
c = 1
if x1 == 1: c |= 1 << 1

costs[c][1] = 0
heap = [(0, 1, c)]
while heap:
    c, node, check = heappop(heap)

    if costs[check][node] < c: continue
    for tnode, tc in graph[node]:
        tcheck = check
        if tnode == x1: tcheck |= 1 << 1
        if tnode == x2: tcheck |= 1 << 2
        
        if costs[tcheck][tnode] <= tc + c: continue
        costs[tcheck][tnode] = tc + c
        heappush(heap, (tc + c, tnode, tcheck))
if costs[(1 << 3) - 1][n] == 0x7fffffff:
    print(-1)
else:
    print(costs[(1 << 3) - 1][n])