# https://www.acmicpc.net/problem/13460
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
a = []
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
back = [1, 0, 3, 2]

# 4차원 배열로 체크해도 되지만 속도 때문에 집합 자료형을 사용하였다
check = set()
rx, ry = -1, -1
bx, by = -1, -1
hx, hy = -1, -1

for i in range(n):
    a.append(list(input().strip()))
    for j in range(m):
        if a[i][j] == 'B':
            bx, by = i, j
            a[i][j] = '.'
        if a[i][j] == 'R':
            rx, ry = i, j
            a[i][j] = '.'
        if a[i][j] == 'O':
            hx, hy = i, j

# 큐에는 빨간공 파란공 위치순으로 삽입되므로
# 위치가 바뀌었다면 swi 변수를 통해 구분합니다.
swi = False

def squence(rx, ry, bx, by, key): # 기울이는 벽쪽과 가장 가까운 공이 가장 앞에 오도록 순서를 바꾸어주는 함수 
    global swi
    x1, y1, x2, y2 = 0, 0, 0, 0
    # key가 북쪽방향이면 x가 더 작은 것부터 이동
    if key == 0:
        if rx >= bx:
            x1, y1, x2, y2 = bx, by, rx, ry
            swi = True
        else:
            x1, y1, x2, y2 = rx, ry, bx, by
    # key가 남쪽이라면 x가 큰 것부터 이동
    elif key == 1:
        if rx >= bx:
            x1, y1, x2, y2 = rx, ry, bx, by
        else:
            x1, y1, x2, y2 = bx, by, rx, ry
            swi = True

    # key가 서쪽이라면 y가 작은 것부터
    elif key == 2:
        if ry >= by:
            x1, y1, x2, y2 = bx, by, rx, ry
            swi = True
        else:
            x1, y1, x2, y2 = rx, ry, bx, by

    # key가 동쪽이라면 y가 큰 것부터
    elif key == 3:
        if ry >= by:
            x1, y1, x2, y2 = rx, ry, bx, by
        else:
            x1, y1, x2, y2 = bx, by, rx, ry
            swi = True

    return x1, y1, x2, y2, key

# 기울이는 쪽 벽과 가장 가까운 공부터 움직입니다.
def get(value : tuple, depth):
    key = value[-1]
    result = []

    for i in range(1, 4, 2):
        x, y = value[i-1], value[i]
        while True:
            x, y = x + dire[key][0], y + dire[key][1]
            if a[x][y] != '.':
                if a[x][y] == '#':
                    a[x + dire[back[key]][0]][y + dire[back[key]][1]] = '#'
                    result.extend([x + dire[back[key]][0], y + dire[back[key]][1]])
                else:
                    result.extend([x, y])
                break
    for i in range(1, 4, 2):
        if a[result[i-1]][result[i]] == '#':
            a[result[i-1]][result[i]] = '.'
    result.append(depth)
    return result

que = deque()
que.append([rx, ry, bx, by, 0])
check.add(f'{que[0][:4]}')

while que:
    q, w, e, r, depth = que.popleft()

    # 10번보다 많이 기울였다면 탐색하지 않습니다.
    if depth + 1 > 10 : continue

    for i in range(4):
        temp = get(squence(q,w,e,r, i), depth)

        # 위치가 바뀌었다면 원래대로 돌려놓습니다.
        if swi:
            temp = [temp[2], temp[3], temp[0], temp[1], depth]
            swi = False

        # 빨간공이 구멍에 빠졌다면
        if temp[0] == hx and temp[1] == hy:
            
            # 같이 빠졌으므로 continue
            if temp[2] == hx and temp[3] == hy: continue
            print(temp[-1] + 1)
            exit()

        # 파란공이 먼저 빠졌다면 탐색 x
        elif temp[2] == hx and temp[3] == hy: continue

        # 깊이까지 체크하면 위치 중복 발생
        t1 = str(temp[:4])
        if t1 in check: continue
        temp[-1] = depth + 1
        check.add(t1)
        que.append(temp)
print(-1)