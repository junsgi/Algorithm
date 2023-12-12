# https://www.acmicpc.net/problem/21939
from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
MAX = []
MIN = []
info = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    info[a] = 0
    heappush(MAX, (-b, -a))
    heappush(MIN, (b, a))

n = int(input())
for _ in range(n):
    com = list(input().strip().split())
    if com[0][0] == 'a':
        l, n = int(com[2]), int(com[1])
        heappush(MAX, (-l, -n))
        heappush(MIN, (l, n))

    elif com[0][0] == 'r':
        if com[1] == '-1':
            while info[MIN[0][1]] != 0:
                info[MIN[0][1]] -= 1
                heappop(MIN)
            print(MIN[0][1])
        else:
            while info[MAX[0][1]] != 0:
                info[MAX[0][1]] -= 1
                heappop(MAX)
            print(-MAX[0][1])

    elif com[0][0] == 's':
        info[com[1]] += 1