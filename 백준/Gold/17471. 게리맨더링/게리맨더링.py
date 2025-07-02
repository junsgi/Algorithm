# https://www.acmicpc.net/problem/17471
import sys
from collections import deque
input = sys.stdin.readline
def BFS():
    global n
    que = deque()
    visit = [0] * (n + 1)
    cntA = 0
    cntB = 0
    costA = 0
    costB = 0
    cnt = 0
    for i in range(1, n + 1):
        if cntA + cntB == n: break
        if visit[i]: continue

        cnt += 1
        if cnt >= 3 : return 0x7fffffff

        visit[i] = 1
        que.append(i)
        if i in A :
            cntA += 1
            costA += values[i - 1]
        elif i in B:
            cntB += 1
            costB += values[i - 1]
        while que:
            node = que.popleft()
            for nxt in graph[node]:
                if visit[nxt]: continue

                if i in A:
                    if nxt not in A: continue
                    visit[nxt] = 1
                    cntA += 1
                    costA += values[nxt - 1]
                    que.append(nxt)
                elif i in B:
                    if nxt not in B: continue
                    visit[nxt] = 1
                    cntB += 1
                    costB += values[nxt - 1]
                    que.append(nxt)
        if not (cntA == len(A) or cntB ==len(B)):
            return 0x7fffffff
    return abs(costA - costB)

def BACK(depth):
    global n, ans
    if depth == n:
        if len(A) == 0 or len(B) == 0: return
        res = BFS()
        ans = min(ans, res)
        return

    A.add(depth + 1)
    BACK(depth + 1)
    A.remove(depth + 1)

    B.add(depth + 1)
    BACK(depth + 1)
    B.remove(depth + 1)
    

n = int(input())
values = list(map(int, input().split()))
graph = [None for _ in range(n + 1)]
A = set()
B = set()
ans = 0x7fffffff
for i in range(1, n + 1):
    graph[i] = list(map(int, input().split()))[1:]
BACK(0)
if ans == 0x7fffffff:
    print(-1)
else:
    print(ans)