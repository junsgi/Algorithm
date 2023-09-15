# https://www.acmicpc.net/problem/14503
import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

n, m = map(int, input().split())
rx, ry, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]]
back = [2, 3, 0, 1]
ans = 0

def DFS(x, y, d):
    global ans
    if a[x][y] == 1:
        print(ans)
        exit()
    if not a[x][y]:
        ans += 1
    a[x][y] = -1

    for i in range(1, 5):
        tx, ty = x + dire[d - i][0], y + dire[d - i][1]
        if not a[tx][ty]:
            if d - i < 0:
                DFS(tx, ty, 4 + d - i)
            else:
                DFS(tx, ty, d - i)
    DFS(x + dire[back[d]][0], y + dire[back[d]][1], d)

DFS(rx, ry, d)
