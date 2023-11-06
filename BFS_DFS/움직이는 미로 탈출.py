#https://www.acmicpc.net/problem/16954
import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    que = deque()
    que.append((7, 0, 0))
    visit[0][7][0] = 1
    dire = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    while que:
        x, y, depth = que.popleft()

        for a, b in dire:
            tx, ty = x + a, y + b
            if not (0 <= tx < 8 and 0 <= ty < 8): continue

            # 벽이 있는 곳으로 갈 수 없으므로 continue
            if visit[depth][tx][ty] == 2: continue

            if depth + 1 < 8:
                # 다음 위치에서 벽이랑 부딪히면 continue
                if visit[depth + 1][tx][ty] == 2: continue
                visit[depth + 1][tx][ty] = 1
                que.append((tx, ty, depth + 1))
            else:
                # 0행에 있던 벽이 모두 사라졌다면 단순 방문 체크용으로 사용
                if visit[depth][tx][ty]: continue
                visit[depth][tx][ty] = 1
                que.append((tx, ty, depth))
            
            if tx == 0 and ty == 7: # 다음 위치가 도착지라면 바로 종료
                return 1
    return 0

def DRAW(x, y): # 깊이마다 벽 위치 기록
    for i in range(x, 8):
        visit[i - x][i][y] = 2

graph = []
visit = [[[0] * 8 for _ in range(8)] for _ in range(8)]

# 입력
for i in range(8):
    graph.append(list(input().strip()))
    for j in range(8):
        if graph[i][j] == '#':
            DRAW(i, j)

print(BFS())