# https://school.programmers.co.kr/learn/courses/30/lessons/72413
from collections import deque
answer = float('inf')
def Dijkstra(start, sCost, graph, n):
    que = deque()
    limit = [float('inf')] * (n + 1)
    que.append((start, sCost))
    limit[start] = 0
    while que:
        st, sc = que.popleft()
        for tNode, tCost in graph[st]:
            if limit[tNode] < sc + tCost: continue
            limit[tNode] = sc + tCost
            que.append((tNode, sc + tCost))
    return limit

def DFS(st, value, graph, check, a, b, n):
    global answer
    #check[st] = 1

    # 현재 노드에서 갈라짐
    dij = Dijkstra(st, 0, graph, n)
    temp = value + dij[a] + dij[b]
    if answer <= temp:
        return
    answer = temp
    for node, cost in graph[st]:
        if check[node]: continue
        check[node] = 1
        DFS(node, value + cost, graph, check, a, b, n)
        check[node] = 0
    
    #check[st] = 0

def solution(n, s, a, b, fares):
    global answer
    graph = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)
    for st, ed, cost in fares:
        graph[st].append([ed, cost])
        graph[ed].append([st, cost])
    check[s] = 1
    DFS(s, 0, graph, check, a, b, n)
    return answer
#answer = 0x7fffffff
#print(solution(6,	6,	4,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#answer = 0x7fffffff
#print(solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#answer = 0x7fffffff
#print(solution(6,	2,	6,	4,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


#answer = 0x7fffffff
#print(solution(7, 3,	4,	1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
#
#answer = 0x7fffffff
#print(solution(7, 4,	3,	1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
#
#answer = 0x7fffffff
#print(solution(7, 1,	3,	4,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

answer = 0x7fffffff
print(solution(6,	4,	5,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
answer = 0x7fffffff
print(solution(6,	5,	4,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
answer = 0x7fffffff
print(solution(6,	6,	5,	4,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
"""
1. 시작하자마자 따로 간다.
 - 목적지가 A 다익스트라
 - 목적지가 B 다익스트라
 
2. 현재 노드에서 다음 노드로 이동 후
 - 위 반복 결과를 비교하여 비용이 더 든다면 return
위 반복
"""