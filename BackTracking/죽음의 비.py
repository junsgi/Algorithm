# https://www.acmicpc.net/problem/22944
import sys
from collections import deque
input = sys.stdin.readline
def BFS(x, y, h):
    global ex, ey, N, D
    check = [[0] * N for _ in range(N)]
    que = deque()
    que.append((x, y, h, 0, 0))
    check[x][y] = h
    while que:
        ax, ay, nowHp, nowUm, depth = que.popleft()

        for a, b in dire:
            tx, ty = ax + a, ay + b
            # 다음 위치가 안전지대라면
            if nowHp >= 1 and tx == ex and ty == ey:
                return depth + 1            
            if not (0 <= tx < N and 0 <= ty < N): continue

            nextHp = nowHp
            if graph[tx][ty] == 'U':
                nextUm = D
            else:
                nextUm = nowUm

            if nextUm:
                nextUm -= 1
            else:
                nextHp -= 1

            if nextHp <= 0 or check[tx][ty] >= nextHp + nextUm: continue
            que.append((tx, ty, nextHp, nextUm, depth + 1))
            check[tx][ty] = nextHp + nextUm
    return -1

def BACK(x, y, hp, um,depth):
    global ex, ey, D, ans
    if hp < 0 or depth >= ans : return

    # 현재위치에서 갈 수 있다면
    if abs(x - ex) + abs(y - ey) <= hp + um:
        ans = min(ans, abs(x - ex) + abs(y - ey) + depth)
        return

    for a, b in ums:
        dis = abs(x - a) + abs(y - b)
        # 우산 전까진 비를 맞으므로 -1
        if dis - 1 >= hp + um: continue
        if visit[a][b]: continue
        if dis < um: # 우산 내구도가 충분하다면
            visit[a][b] = 1
            BACK(a, b, hp, D, depth + dis)
            visit[a][b] = 0
        else :
            visit[a][b] = 1
            BACK(a, b, hp - (dis - um), D, depth + dis)
            visit[a][b] = 0

        


N, H, D = map(int, input().split())
visit = [[0] * N for _ in range(N)]
graph = []
ums = []
ans = 0x7fffffff
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
sx, sy, ex, ey = 0, 0, 0, 0
for i in range(N):
    graph.append(list(input()))
    for j in range(N):
        if graph[i][j] == 'S':
            sx, sy = i, j
        if graph[i][j] == 'E':
            ex, ey = i, j
        if graph[i][j] == 'U':
            ums.append([i, j])

#print(BFS(sx, sy, H))
#BACK(sx, sy, H, 0 ,0)
#print(-1 if ans == 0x7fffffff else ans)