# https://www.acmicpc.net/problem/2589
from collections import deque
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
check = [[0] * m for _ in range(n)]
que = deque()
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def BFS(x, y, cn):
    global n, m
    que.clear()
    que.append((x, y, 0))
    check[x][y] = cn
    result = 0
    while que:
        ax, ay, depth = que.popleft()
        result = max(result, depth)
        for a, b in dire:
            tx, ty = ax + a, ay + b
            if not (0 <= tx < n and 0 <= ty < m): continue
            if check[tx][ty] == cn or graph[tx][ty] == 'W':continue
            que.append((tx, ty, depth + 1))
            check[tx][ty] = cn
    return result
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans, BFS(i, j, i + j + 1))
print(ans)