# https://www.acmicpc.net/problem/20058
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
ice = [list(map(int, input().rstrip().split())) for _ in range(2 ** n)]
comm = list(map(int, input().rstrip().split()))
que = deque()
mv = deque()
dire = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 1]]

#def MOVE(x, y, length):
#    temp = [[0] * length for _ in range(length)]
#    tx, ty = 0, 0
#    for i in range(x, x + length):
#        for j in range(y, y + length):
#            temp[ty][length - tx - 1] = ice[i][j]
#            ty += 1
#        tx += 1
#        ty = 0
#    tx = ty = 0
#    for i in range(x, x + length):
#        for j in range(y, y + length):
#            ice[i][j] = temp[tx][ty]
#            ty += 1
#        tx += 1
#        ty = 0

def MOVE(x, y, length, size):
    mv.clear()
    while length != 0:
        tx, ty = x, y
        for idx in range(4 if length == 2 else 5):
            for cnt in range(length):
                if idx == 0:
                    mv.append(ice[tx][ty])
                    ice[tx][ty] = -1
                else:
                    value = ice[tx][ty]
                    if mv and not (cnt == 0 and value != -1) :
                        ice[tx][ty] = mv.popleft()
                        if value != -1:
                            mv.append(value)
                
                if cnt == length - 1: break

                tx += dire[idx][0]
                ty += dire[idx][1]
        length -= 2
        size //= 4
        x += 1
        y += 1
        
def count(x, y, length):
    c = 0
    for a, b in dire[:-1]:
        tx, ty = x + a, y + b
        if not (0 <= tx < length and 0 <= ty < length) or ice[tx][ty] == 0: continue
        c += 1
    return c < 3
def melt(length):
    result = []
    for i in range(length):
        for j in range(length):
            if ice[i][j] > 0 and count(i, j, length):
                result.append((i, j))
    for i, j in result:
        ice[i][j] -= 1

def div(x, y, length, size):
    global target
    if size == target:
        MOVE(x, y, length)
        return

    l = length // 2
    s = size // 4
    # 분할정복
    div(x, y, l, s)
    div(x, y + l, l, s)
    div(x + l, y, l, s)
    div(x + l, y + l , l, s)

check = [[0] * 2 ** n for _ in range(2 ** n)]
def BFS(x, y, length):
    que.clear()
    que.append((x, y))
    check[x][y] = 1
    result = 1
    while que:
        ax, ay = que.popleft()
        for a, b in dire:
            tx, ty = ax + a, ay + b
            if not (0 <= tx < length and 0 <= ty < length): continue
            if check[tx][ty] or ice[tx][ty] == 0 : continue
            result += 1
            que.append((tx, ty))
            check[tx][ty] = 1
    return result

for c in comm:
    target = (2 ** c) ** 2
    if c != 0:
        div(0, 0, 2 ** n, (2 ** n) ** 2)
    melt(2 ** n)

r1 = 0
r2 = 0
for i in ice:
    r1 += sum(i)

for i in range(2 ** n):
    for j in range(2 ** n):
        if ice[i][j] != 0 and check[i][j] == 0:
            r2 = max(r2, BFS(i, j, 2 ** n))
print(r1, r2, sep = '\n')
#for i in ice:
    #print(*i)