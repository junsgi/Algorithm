# https://school.programmers.co.kr/learn/courses/30/lessons/72413
from collections import deque
answer = float('inf')
def Dijkstra(start, graph, n):
    que = deque()
    limit = [float('inf')] * (n + 1)
    que.append((start, 0))
    limit[start] = 0
    while que:
        s1, s2 = que.popleft()
        if limit[s1] < s2: continue
        for tNode, tCost in graph[s1]:
            if limit[tNode] < s2 + tCost: continue
            limit[tNode] = s2 + tCost
            que.append((tNode, s2 + tCost))
    return limit 
# 빠르지만 정답이 나오지 않는 코드
# def DFS(st, value, graph, check, a, b, n):
#     global answer
#     if value >= answer:
#         return
#     # k -> A
#     # k -> B (현재 노드에서 갈라지는 경우)
#     dij = Dijkstra(st, graph, n)
#     temp = value + dij[a] + dij[b]
#     if answer <= temp:
#         return
#     answer = temp
#     check[st] = 1
#     for node, cost in graph[st]:
#         if check[node]: continue
#         # s -> k (다음 노드에서)
#         DFS(node, value + cost, graph, check, a, b, n)
#     check[st] = 0

def solve(st, a, b, n, graph):
    # k -> A
    # k -> B (현재 노드에서 갈라지는 경우)
    ans = 0x7fffffff
    dij = [Dijkstra(st, graph, n), Dijkstra(a, graph, n), Dijkstra(b, graph, n)]
    for i in zip(dij[0], dij[1], dij[2]):
        if i[0] == float('inf'): continue
        ans = min(ans, sum(i))
    return ans

def solution(n, s, a, b, fares):
    global answer
    graph = [[] for _ in range(n + 1)]
    for st, ed, cost in fares:
        graph[st].append([ed, cost])
        graph[ed].append([st, cost])
    #DFS(s, 0, graph, check, a, b, n)
    return solve(s, a, b, n, graph)