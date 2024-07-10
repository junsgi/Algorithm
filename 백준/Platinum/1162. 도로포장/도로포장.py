import sys
from collections import defaultdict 
from heapq import heappush, heappop
input = sys.stdin.readline
MAX = 20_000_000_000
def dijkstra(n, k, graph):
  heap = [(0, 1, 0)]
  cost = [[MAX] * (n + 1) for _ in range(k + 1)]
  cost[0][1] = 0
  answer = MAX
  while heap:
    value, node, cnt = heappop(heap)
    if node == n:
      answer = min(answer, value)
      continue
    if cost[cnt][node] < value:
      continue
    for tnode, tvalue in graph[node]:
      if cost[cnt][tnode] > value + tvalue:
        cost[cnt][tnode] = value + tvalue
        heappush(heap, (cost[cnt][tnode], tnode, cnt))
      if cnt != k and cost[cnt + 1][tnode] > value:
        cost[cnt + 1][tnode] = value
        heappush(heap, (cost[cnt + 1][tnode], tnode, cnt + 1))
  return answer
n, m, k = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(m):
  st, ed, c = map(int, input().strip().split())
  graph[st].append((ed, c))
  graph[ed].append((st, c))
print(dijkstra(n, k, graph))