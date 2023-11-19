# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visit = [0] * (n + 1)
    MAX = 0
    for st, ed in edge:
        graph[st].append(ed)
        graph[ed].append(st)
    visit[1] = 1
    que = deque()
    que.append([1, 0])
    while que:
        node, depth = que.popleft()

        for nxt in graph[node]:
            if visit[nxt]: continue
            visit[nxt] = depth + 1
            MAX = max(MAX, visit[nxt])
            que.append([nxt, depth + 1])
    return visit[1:].count(MAX)