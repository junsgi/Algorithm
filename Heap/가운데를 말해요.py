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
    # 입력 값 + 중앙 값 + 두 힙 크기가 홀수라면
    if len(MAX) == len(MIN):
        heappush(MIN, t1)
        heappush(MAX, -t2)
        mid = -heappop(MAX)
    else: # 입력 값 + 중앙 값 + 두 힙 크기가 홀수라면

        # 최소힙의 길이가 더 짧다면
        if len(MAX) < len(MIN): 
            if mid <= x:
                heappush(MIN, t2)
            else:
                pass
        else:pass


    print(mid)
