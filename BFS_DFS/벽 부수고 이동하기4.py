# https://www.acmicpc.net/problem/16946
import sys
input = sys.stdin.readline
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def BFS(x, y, area):
    global n, m
    que = []
    front = -1
    que.append((x, y))
    DP[x][y][1] = 1
    while front + 1 < len(que):
        front += 1
        ax, ay = que[front]
        for a, b in dire:
            tx, ty = ax + a, ay + b
            if not (0 <= tx < n and 0 <= ty < m): continue
            if graph[tx][ty] or DP[tx][ty][1] : continue
            DP[tx][ty][1] = 1
            que.append((tx, ty))
    for tx, ty in que:
        DP[tx][ty] = [front + 1, area]

n, m = map(int, input().split())
DP = [[[0, 0] for __ in range(m)] for _ in range(n)]
graph = []
info = [[], []]
for i in range(n):
    arr = list(map(int, list(input().strip())))
    graph.append(arr)
    for j in range(m):
        info[arr[j]].append((i, j))
area = 0
for x, y in info[0]:
    if DP[x][y][1] == 0:
        area += 1
        BFS(x, y, area)
cnt = 1
visit = [0] * (area + 1)
for x, y in info[1]:
    if x + 1 < n and visit[DP[x + 1][y][1]] != cnt:
        visit[DP[x + 1][y][1]] = cnt
        graph[x][y] += DP[x + 1][y][0]

    if x - 1 >= 0 and visit[DP[x - 1][y][1]] != cnt: 
        visit[DP[x - 1][y][1]] = cnt
        graph[x][y] += DP[x - 1][y][0]

    if y + 1 < m and visit[DP[x][y + 1][1]] != cnt: 
        visit[DP[x][y + 1][1]] = cnt
        graph[x][y] += DP[x][y + 1][0]

    if y - 1 >= 0 and visit[DP[x][y - 1][1]] != cnt: 
        visit[DP[x][y - 1][1]] = cnt
        graph[x][y] += DP[x][y - 1][0]
    cnt += 1
    graph[x][y] %= 10
for i in graph:
    for j in i:
        print(j,end='')
    print()