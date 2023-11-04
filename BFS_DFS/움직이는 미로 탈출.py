#https://www.acmicpc.net/problem/16954
import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    que = deque()
    que.append((7, 0, 0))
    visit[0][7][0] = 1
    dire = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    while que:
        x, y, cnt = que.popleft()
        if x == 0 and y == 7:
            return 1
        for a, b in dire:
            tx, ty = x + a, y + b
            if not (0 <= tx < 8 and 0 <= ty < 8 and cnt + 1 <= 8): continue
            if visit[cnt + 1][tx][ty] or visit[cnt][x][y] + 1 >= check[cnt + 1][tx][ty]: continue
            visit[cnt + 1][tx][ty] = visit[cnt][x][y] + 1
            que.append((tx, ty, cnt + 1))
    return 0
def DRAW(x, y):
    c = 0
    for i in range(8):
        c = i
        for j in range(x + i, 8):
            check[i][j][y] = check[j][i][y] = c
            c += 1
graph = []
MAX = 0x7fffffff
visit = [[[0] * 8 for _ in range(8)] for _ in range(9)]
check = [[[MAX] * 8 for _ in range(8)] for _ in range(9)]
for i in range(8):
    graph.append(list(input().strip()))
    for j in range(8):
        if graph[i][j] == '#':
            DRAW(i, j)
for i in check:
    for j in i:
        for k in j:
            print(f"{k:11d}", end = '')
        print()
    print()

print("\nvisit\n")
n = BFS()
for i in visit:
    for j in i:
        for k in j:
            print(f"{k:3d}", end = '')
        print()
    print()
print(n)
