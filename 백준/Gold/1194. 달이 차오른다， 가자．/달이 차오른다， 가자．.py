from collections import deque
def BFS(n, m, sx, sy, graph):
    dire = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visit = [[[0 for _ in range(m)] for __ in range(n)] for ___ in range(1 << 7)]
    que = deque()

    visit[0][sx][sy] = 1
    que.append((sx, sy, 0))
    while que:
        x, y, key = que.popleft()

        for a, b in dire:
            tx, ty = x + a, y + b
            if not (0 <= tx < n and 0 <= ty < m): continue
            if graph[tx][ty] == "#": continue
            
            k = ord(graph[tx][ty]) - 97
            K = ord(graph[tx][ty]) - 65
            if graph[tx][ty] == '1':
                return visit[key][x][y]
            elif graph[tx][ty] == "." and not visit[key][tx][ty]:
                visit[key][tx][ty] = visit[key][x][y] + 1
                que.append((tx, ty, key))

            elif 'A' <= graph[tx][ty] <= 'F' and key & (1 << K) != 0 and visit[key][tx][ty] == 0:
                visit[key][tx][ty] = visit[key][x][y] + 1
                que.append((tx, ty, key))

            elif 'a' <= graph[tx][ty] <= 'f' and not visit[key | (1 << k)][tx][ty]:
                visit[key | (1 << k)][tx][ty] = visit[key][x][y] + 1
                que.append((tx, ty, key | (1 << k)))
    return -1
                



n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "0":
            graph[i][j] = "."
            sx, sy = i, j

print(BFS(n, m, sx, sy, graph))
