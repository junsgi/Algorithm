# https://www.acmicpc.net/problem/1655
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def get(cnt):
    result = []
    for _ in range(cnt):
        num = heappop(heap)
        result.append(num)
    n = result[-1]
    while result:
        heappush(heap, result.pop())
    return n
heap = []

n = int(input())
x = int(input())
print(x)
heappush(heap, x)
for _ in range(n - 1):
    x = int(input())
    heappush(heap, x)
    if len(heap) % 2:
        print(get(len(heap) // 2 + 1))
    else:
        print(get(len(heap) // 2))


"""
left, mid, right
1
1, 0, 0

5
1, 5, 0
1, 2, 5
1, 2, 10
-99, 2, 10


"""