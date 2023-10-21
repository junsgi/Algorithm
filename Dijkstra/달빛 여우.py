# https://www.acmicpc.net/problem/16118
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().strip().split())
    graph[s].append([e, c])
    graph[e].append([s, c])

wolf = [[float("inf")] * (n + 1) for _ in range(3)]
fox = [float("inf")] * (n + 1)
fox[1] = 0
wolf[1][1] = 0
que = deque()
que.append((0, 1, 0))
que.append((2, 1, 0))
while que:
    status, node, cost = que.popleft()
    if status == 0 and fox[node] < cost: continue
    if status >= 1 and wolf[status][node] < cost: continue
    for nx, tc in graph[node]:
        if status == 0: # 여우면
            if fox[nx] <= tc + cost: continue
            fox[nx] = tc + cost
            que.append((status, nx, tc + cost))
        elif status == 2: # 빠른 늑대라면
            if wolf[1][nx] <= cost + tc // 2: continue
            wolf[1][nx] =  cost + tc // 2 if cost + tc // 2 else 1
            que.append((1, nx, cost + tc // 2))
        else: # 느린 늑대라면
            if wolf[2][nx] <= cost + tc * 2: continue
            wolf[2][nx] = cost + tc * 2
            que.append((2, nx, cost + tc * 2))
ans = 0
for i in range(2, n + 1):
    if wolf[1][i] + wolf[2][i] + fox[i] == float('inf'):continue
    if fox[i] < min(wolf[1][i], wolf[2][i]):
        ans += 1
print(ans)
"""
5 5
1 2 1
1 4 5
1 5 3
4 5 4
2 3 400

5 6
1 2 3
1 3 2
2 3 2
2 4 4
3 5 4
4 5 3


"""