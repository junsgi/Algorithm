import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().strip().split())
pool = []
"""
1. 입력으로 주어진 수영장을 실제 3차원 배열로 구현
2. 1층부터 9층까지 벽이 아니라면 큐에 삽입
3. 방문 배열의 물의 개수를 구함
"""

visit = [[[0 for i in range(m + 2)] for j in range(n + 2)] for k in range(10)]
limit = 0
for i in range(n):
    pool.append(list(map(int, input().strip())))
    for j in range(m):
        # 현재 입력한 높이중 가장 높은 값을 구함
        limit = max(limit, pool[i][j])

        # 입력대로 수영장 만듦
        for k in range(1, pool[i][j] + 1):
            visit[k][i + 1][j + 1] = 1


que = deque()
def BFS():
    global n, m, limit
    dire = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1]]

    que.append((0, 0, 1))

    while que:
        x, y, z = que.popleft()
        for a, b, c in dire:
            tx, ty, tz = a + x, b + y, c + z
            if not (0 <= tx <= n + 1 and 0 <= ty <= m + 1 and 1 <= tz <= limit): continue
            if visit[tz][tx][ty]:
                continue
            visit[tz][tx][ty] = 1
            que.append((tx, ty, tz))
        
BFS()
ans = 0
# 물의 개수(0)를 구합니다.
for w in range(1, limit + 1):
    for i in visit[w]:
        ans += i.count(0)
print(ans)
