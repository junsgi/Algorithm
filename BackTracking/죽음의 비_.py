# https://www.acmicpc.net/problem/22944
import sys
from collections import deque
input = sys.stdin.readline
N, H, D = map(int, input().split())
graph = []
sx, sy, ex, ey = 0, 0, 0, 0
for i in range(N):
    graph.append(list(input()))
    for j in range(N):
        if graph[i][j] == 'S':
            sx, sy = i, j
        if graph[i][j] == 'E':
            ex, ey = i, j
check = [[[0] * N for _ in range(N)] for __ in range(11)]
que = deque()
que.append((sx, sy, 0, 0))
check[0][sx][sy] = H
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while que:
    ax, ay, depth, umHp = que.popleft()
    if ax == ex and ay == ey:
        print(depth)
        exit()
    if graph[ax][ay] == 'U' and not check[D][ax][ay]:
        check[D][ax][ay] = check[umHp][ax][ay]
        que.append((ax, ay, depth, D))
    for a, b in dire:
        tx, ty = ax + a, ay + b
        if not (0 <= tx < N and 0 <= ty < N): continue

        if graph[ax][ay] == 'S':
            check[umHp][tx][ty] = check[umHp][ax][ay]
            que.append((tx, ty, depth + 1, umHp))
        else:
            # 우산 내구도
            if umHp - 1 >= 0 and not check[umHp - 1][tx][ty]:
                check[umHp - 1][tx][ty] = check[umHp][ax][ay]
                que.append((tx, ty, depth + 1, umHp - 1))
            elif check[umHp][ax][ay] - 1 > 0 and not check[umHp][tx][ty]:
                check[umHp][tx][ty] = check[umHp][ax][ay] - 1
                que.append((tx, ty, depth + 1, umHp))


print(-1)