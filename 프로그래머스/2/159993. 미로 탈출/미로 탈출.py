def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    visit = [[[0] * M for _ in range(N)] for __ in range(2)]
    que = [None] * (N * M * 2)
    front, rear = -1, -1
    for i in range(N):
        f = 0
        for j in range(M):
            if maps[i][j] == "S":
                f = 1
                que[(rear := rear + 1)] = (i, j, 0)
                visit[0][i][j] = 1
                break
        if f: break
    
    while front != rear:
        x, y, c = que[(front := front + 1)]
        if c == 1 and maps[x][y] == "E":
            return visit[c][x][y] - 1
        if maps[x][y] == "L" and visit[1][x][y] == 0:
            que[(rear := rear + 1)] = (x, y, 1)
            visit[1][x][y] = visit[c][x][y]
        if x + 1 < N and maps[x + 1][y] != "X" and visit[c][x + 1][y] == 0:
            que[(rear := rear + 1)] = (x + 1, y, c)
            visit[c][x + 1][y] = visit[c][x][y] + 1
        if 0 <= x - 1 and maps[x - 1][y] != "X" and visit[c][x - 1][y] == 0:
            que[(rear := rear + 1)] = (x - 1, y, c)
            visit[c][x - 1][y] = visit[c][x][y] + 1
        if y + 1 < M and maps[x][y + 1] != "X" and visit[c][x][y + 1] == 0:
            que[(rear := rear + 1)] = (x, y + 1, c)
            visit[c][x][y + 1] = visit[c][x][y] + 1
        if 0 <= y - 1 and maps[x][y - 1] != "X" and visit[c][x][y - 1] == 0:
            que[(rear := rear + 1)] = (x, y - 1, c)
            visit[c][x][y - 1] = visit[c][x][y] + 1
    return -1