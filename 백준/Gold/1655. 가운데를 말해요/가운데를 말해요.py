# https://www.acmicpc.net/problem/1655
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
MAX = []
MIN = []
mid = int(input())
print(mid)
for i in range(n - 1):
    x = int(input())

    t1, t2 = max(mid, x), min(mid, x)
    heappush(MIN, t1)
    heappush(MAX, -t2)
    
    if len(MAX) != len(MIN):
        if len(MAX) > len(MIN):
            mid = -heappop(MAX)
        else:
            mid = heappop(MIN)
    else:
        mid = -heappop(MAX)
    print(mid)