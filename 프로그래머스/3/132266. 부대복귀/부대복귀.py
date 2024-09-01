from collections import defaultdict
from heapq import heappush, heappop
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for st, ed in roads:
        graph[st].append(ed)
        graph[ed].append(st)
    cost = [0x7fffffff] * (n + 1)
    cost[destination] = 0
    heap = [(0, destination)]
    while heap:
        depth, node = heappop(heap)
        if cost[node] < depth: continue
        for tnode in graph[node]:
            if cost[tnode] < depth + 1: continue
            cost[tnode] = depth + 1
            heappush(heap, (cost[tnode], tnode))
    for i in sources:
        if cost[i] == 0x7fffffff:
            answer.append(-1)
        else:
            answer.append(cost[i])
    return answer