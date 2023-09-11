# https://www.acmicpc.net/problem/14503
import sys
sys.setrecursionlimit(200)
input = sys.stdin.readline

n, m = map(int, input().split())
rx, ry, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dire = [[-1, 0],[0, 1], [1, 0], [0, -1]]
back = [2, 3, 0, 1]
ans = 0
def BACK(x, y, d):
    pass
def MOVE(x, y, d):
    global ans
    a[x][y] = -1
    ans += 1

    tx, ty = x + dire[d][0], y + dire[d][0]
    if a[tx][ty] == 0:
        MOVE(tx, ty, d)
    else:
        BACK(x, y, d)


MOVE(rx, ry, d)
print(ans)