# https://www.acmicpc.net/problem/2252
from collections import deque
n, m = map(int, input().split())
visit = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    visit[ed] += 1
que = deque()
for i in range(1, n + 1):
    if visit[i] == 0:
        que.append(i)
answer = ""

while que:
    node = que.popleft()
    answer += str(node) + " "

    for nxt in graph[node]:
        if visit[nxt] != 0:
            visit[nxt] -= 1
        if visit[nxt] == 0:
            que.append(nxt)
print(answer)
    