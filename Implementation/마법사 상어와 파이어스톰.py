# https://www.acmicpc.net/problem/20058
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
ice = [list(map(int, input().rstrip().split())) for _ in range(2 ** n)]
comm = list(map(int, input().rstrip().split()))
que = deque()

def div(x, y, length, size):
    global target
    if size == target:
        pass

    l = length // 2
    s = size // 4
    # 분할정복
    div(x, y, l, s)
    div(x, y + l, l, s)
    div(x + l, y, l, s)
    div(x + l, y + l , l, s)

for c in comm:
    target = 2 ** c

    div(0, 0, n ** 2, n ** 2)

arr = [[i + j * 4 for i in range(1, 5)] for j in range(4)]
for a in arr:print(a)
limit = 4
cnt = 0
dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
temp = deque()
for i in range(4, 1, -2):
    x, y = cnt, cnt
    for j in range(4):
        for z in range(i):
            pass
print()
for a in arr:print(a)