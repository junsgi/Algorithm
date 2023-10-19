# https://www.acmicpc.net/problem/1826
from heapq import heappush, heappop
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
target, cOil = map(int, input().split())
arr.sort(key = lambda x : x[0])
arr.append([target, 0])
ans = 0
heap = []
for i in range(n + 1):
    dis, oil = arr[i]
    if cOil - dis < 0:
        while heap and cOil - dis < 0:
            ans += 1
            cOil += -heappop(heap)
    if not heap and cOil - dis < 0:
        ans = -1
        break
    else:
        heappush(heap, -oil)
print(ans)