# https://www.acmicpc.net/problem/2468
from collections import deque
import sys
sys.setrecursionlimit(10001)
def BFS(x, y, visit, limit):
    global n
    que.clear()
    que.append((x, y))
    visit[x][y] = 1
    while que:
        ax, ay = que.popleft()
        for i, j in dire:
            tx, ty = ax + i, ay + j
            if not (0 <= tx < n and 0 <= ty < n): continue
            if visit[tx][ty] or arr[tx][ty] > limit:continue
            visit[tx][ty] = 1
            que.append((tx, ty))

def DFS(x, y, visit):
    for i, j in dire:
        tx, ty = x + i, y + j
        if not (0 <= tx < n and 0 <= ty < n): continue
        if visit[tx][ty] != 0 : continue
        visit[tx][ty] = 1
        DFS(tx, ty, visit)
    
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
maxHeight = 0
for lst in arr:
    maxHeight = max(maxHeight, max(lst))
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
que = deque()
ans = 0
for height in range(maxHeight + 1):
    check = [[0] * n for _ in range(n)]
    # height 이하 체크
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= height and check[i][j] == 0:
                BFS(i, j, check, height)
    # 영역 개수
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                cnt += 1
                check[i][j] = 1
                DFS(i, j, check)
    ans = max(cnt, ans)
print(ans)