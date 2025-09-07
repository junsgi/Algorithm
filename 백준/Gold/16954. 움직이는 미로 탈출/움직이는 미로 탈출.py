#https://www.acmicpc.net/problem/16954
import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    global MAX
    que = deque()
    que.append((7, 0, 0))
    visit[0][7][0] = 1
    dire = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    while que:
        x, y, cnt = que.popleft()
        #if cnt + 1 < 8 and not visit[cnt + 1][x][y] and visit[cnt][x][y] + 1 < check[cnt + 1][x][y]:
        #    visit[cnt + 1][x][y] = visit[cnt][x][y] + 1
        #    que.append((x, y, cnt + 1, depth))

        for a, b in dire:
            tx, ty = x + a, y + b
            if not (0 <= tx < 8 and 0 <= ty < 8): continue
            if check[cnt][tx][ty]: continue
            if cnt + 1 < 8:
                if not (not check[cnt + 1][tx][ty] and not visit[cnt + 1][tx][ty]): continue
                visit[cnt + 1][tx][ty] = 1
                que.append((tx, ty, cnt + 1))
            else:
                if visit[cnt][tx][ty]: continue
                visit[cnt][tx][ty] = 1
                que.append((tx, ty, cnt))
            
            if tx == 0 and ty == 7:
                return 1
    return 0
def DRAW(x, y):
    global MAX
    for i in range(x, 8):
        check[i - x][i][y] = 1
graph = [list(input().strip()) for _ in range(8)]
MAX = 0x7fffffff
visit = [[[0] * 8 for _ in range(8)] for _ in range(8)]
check = [[[0] * 8 for _ in range(8)] for _ in range(8)]

for i in range(7, -1, -1):
    for j in range(8):
        if graph[i][j] == '#':
            DRAW(i, j)

print(BFS())

