# https://www.acmicpc.net/problem/25969
import sys
from collections import deque
input = sys.stdin.readline
dtemp = [(i, j) for i in range(-2, 3) for j in range(-2, 3)]
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
skill = []

n, m, k = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
idx = 0
for i in range(5):
    lst = list(map(int, input().strip().split()))
    for j in lst:
        if j == 1:
            skill.append(dtemp[idx])
        idx += 1
que = deque()
check =[[[[0] * m for _ in range(n)] for __ in range(k + 1)] for ___ in range(2)]
# 큐에 넣는 경우
# 추가 패턴을 사용하지 않고 상하좌우로 탐색
# 추가 패턴을 사용할 수 있으면 능력을 사용하면서 탐색
# 중간 거점지를 만났으면 탐색
que.append((0, 0, 0, 0, 0))
check[0][0][0][0] = 1
while que:
    x, y, depth, cnt, visit = que.popleft()

    if visit == 1 and x == n - 1 and y == m - 1:
        print(depth)
        exit()

    if graph[x][y] == 2 and check[1][cnt][x][y] == 0:
        que.append((x, y, depth, cnt, 1))
        check[1][cnt][x][y] = 1

    for a, b in dire:
        tx, ty = x + a, y + b
        if not ( 0 <= tx < n and 0 <= ty < m) : continue
        if check[visit][cnt][tx][ty] == 1 or graph[tx][ty] == 1: continue
        que.append((tx, ty, depth + 1, cnt, visit))
        check[visit][cnt][tx][ty] = 1

    if cnt + 1 <= k:
        for a, b in skill:
            tx, ty = x + a, y + b
            if not ( 0 <= tx < n and 0 <= ty < m) : continue
            if check[visit][cnt + 1][tx][ty] == 1 or graph[tx][ty] == 1: continue
            que.append((tx, ty, depth + 1, cnt + 1, visit))
            check[visit][cnt + 1][tx][ty] = 1
print(-1)