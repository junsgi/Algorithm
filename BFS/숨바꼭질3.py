# https://www.acmicpc.net/problem/13549
from collections import deque
n, m = map(int, input().split())
check = set()
que = deque()
def BFS(n, m):
    que.append((n, 0))
    check.add(n)

    while que:
        num, time = que.popleft()
        if num == m:
            return time
        if num * 2 in check or num * 2 <= 100000 :
            que.append((num * 2, time))
            check.add(num * 2)
            
        if num - 1 not in check and num - 1 >= 0:
            que.append((num - 1, time + 1))
            check.add(num - 1)

        if num + 1 not in check and num + 1 <= 100000:
            que.append((num + 1, time + 1))
            check.add(num + 1)

        
print(BFS(n, m))