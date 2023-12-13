# https://www.acmicpc.net/problem/1005
"""
위상 정렬 + DP + BFS
"""
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def search(cost, visit, graph, END, n):
    que = deque()
    for i in range(1, n + 1):
        if visit[i] == 0:
            que.append(i)
            visit[i] = -1
    
    while que:
        node = que.popleft()
        if node == END:
            return
        for nxd in graph[node]:
            # 방문 했던 곳은 탐색하지 않습니다.
            if visit[nxd] == -1: continue

            # 최단거리로 다음 건물을 건설할 수 있더라도 
            # 다음 건물과 연결된 건물들이 있을 수 있으므로 최대값으로만 대입합니다.
            times[nxd] = max(times[nxd], times[node] + cost[nxd])

            # 위상 정렬
            if visit[nxd] != 0:
                visit[nxd] -= 1
            if visit[nxd] == 0:
                visit[nxd] = -1
                que.append(nxd)


for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    visit = [0] * (n + 1)
    times = cost[:]
    graph = defaultdict(list)
    for __ in range(k):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        visit[ed] += 1
    END = int(input())
    search(cost, visit, graph, END, n)
    print(times[END])
