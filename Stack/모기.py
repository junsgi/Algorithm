# https://www.acmicpc.net/problem/20440
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : x[0])
stk = []
ans = []
for st, ed in arr:
    if not stk or stk[-1][1] > st:
        stk.append([st, ed])
    else:
        temp = [-len(stk), 0, 1e12]
        while stk and stk[-1][1] <= st:
            e = stk.pop()
            temp[1] = max(temp[1], e[0])
            temp[2] = min(temp[2], e[1])
        stk.append([st, ed])
        heappush(ans, temp)

if stk:
    temp = [-len(stk), stk[-1][0],stk[-1][1]]
    stk.pop()
    while stk:
        e = stk.pop()
        temp[1] = max(temp[1], e[0])
        temp[2] = min(temp[2], e[1])
    heappush(ans, temp)
result = heappop(ans)
print(-result[0])
print(result[1], result[2])