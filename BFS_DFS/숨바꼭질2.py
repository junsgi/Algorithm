# https://www.acmicpc.net/problem/12851
from collections import deque
n, m = map(int, input().split())

que = deque()
ans = 0
def BFS(n, m, limit = -1):
    global ans
    que.clear()
    check = [0] * (m * 2)
    que.append((n, 0))
    check[n] = 1
    while que:
        num, time = que.popleft()
        if limit == -1 and num == m:
          return time
        if limit != -1 and limit == time and num == m:
            ans += 1
        if limit != -1 and limit < time + 1: continue
        
        if 0 <= num * 2 <= m * 2 and num * 2 and not check[num * 2]:
            que.append((num * 2, time + 1))
            if limit == -1 :
                check[num * 2] = 1

        if num - 1 >= 0 and num - 1 and not check[num - 1]:
            que.append((num - 1, time + 1))
            if limit == -1: 
                check[num - 1] = 1

        if num + 1 <= m and num + 1 and not check[num + 1]:
            que.append((num + 1, time + 1))
            if limit == -1: 
                check[num + 1] = 1

if n > m:
    time = n - m
    ans = 1
else:
    time = BFS(n, m)
    BFS(n, m, limit=time)
print(time, ans , sep='\n')