# https://www.acmicpc.net/problem/1916
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
ck = 0
for _ in range(m):
    st, ed, cost = map(int, input().split())
    graph[st].append([ed, cost])
st, ed = map(int, input().split())

que = deque()
check = [float("inf")] * (n + 1)
que.append((st, 0))
check[st] = 0
while que:
    dis, cost = que.popleft()
    if check[dis] < cost: continue
    for value, tcost in graph[dis]:
        if check[value] <= tcost + cost: continue
        check[value] = tcost + cost
        que.append((value, tcost + cost))
print(check[ed])