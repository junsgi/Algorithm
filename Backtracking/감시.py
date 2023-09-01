import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().strip().split())
a = []
sum = n * m
cctv = 0
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
check = [
    [0, 1, 2, 3],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]]
]
que = deque()
tque = deque()
for i in range(n):
    a.append(list(map(int, input().strip().split())))
    for j in range(m):
        if 1 <= a[i][j] <= 6:
            sum -= 1
            if a[i][j] != 6:
                que.append((i, j, a[i][j]))

for i in range(n):
    for j in range(m):
        if a[i][j] == 5:
            for t1, t2 in dire:
                cnt = 1
                while True:
                    tx, ty = i + t1 * cnt, j + t2 * cnt
                    if not (0 <= tx < n and 0 <= ty < m) : break
                    if a[tx][ty] == 6: break
                    sum -= 1
                    cnt += 1

def back(depth, sum):
    tsum = sum
    if que[depth][2] == 1:
        for tx, ty in dire:
            cnt = 1
            while True:
                tx, ty = i + t1 * cnt, j + t2 * cnt
                if not (0 <= tx < n and 0 <= ty < m) : break
                if a[tx][ty] == 6: break
                cnt += 1