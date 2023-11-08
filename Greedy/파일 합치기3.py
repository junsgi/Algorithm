# https://www.acmicpc.net/problem/13975
from heapq import heappush, heappop
n = int(input())
for _ in range(n):
    LEN = int(input())
    arr = list(map(int, input().split()))