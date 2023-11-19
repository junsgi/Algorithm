#https://www.acmicpc.net/problem/15971
"""
2번 로봇에 도착하면 왔던 길 중 가장 길었던 길만 빼면된다.
"""
from collections import deque
import sys
input = sys.stdin.readline
n, r1, r2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    st, ed, cost = map(int, input().split())
    graph[st].append([ed, cost])
    graph[ed].append([st, cost])
visit = [0] * (n + 1)
que = deque()
visit[r1] = 1
que.append([r1, 0, 0])
answer = 0
while que:
    node, value, MAX = que.popleft()
    if node == r2:
        answer = value - MAX
        break
    for nx, nc in graph[node]:
        if visit[nx]:continue
        visit[nx] = 1
        que.append([nx, value + nc, max(MAX, nc)])
print(answer)