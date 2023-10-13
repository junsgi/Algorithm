# https://www.acmicpc.net/problem/12851
from collections import deque
n, m = map(int, input().split())
que = deque()
check = [[-1, 0] for _ in range(100001)]
def BFS(n):
    global ans
    que.append((n, 0))
    check[n][0] = 0
    check[n][1] = 1
    while que:
        value, time = que.popleft()
        for i in [value * 2, value - 1, value + 1]:
            if not(0 <= i <= 100000):continue
            if check[i][0] == -1:
                check[i][0] = time + 1
                check[i][1] = 1
                que.append((i, time + 1))
            elif check[i][0] == time + 1:
                check[i][1] += 1
                que.append((i, time + 1))

BFS(n)
print(check[m][0])
print(check[m][1])