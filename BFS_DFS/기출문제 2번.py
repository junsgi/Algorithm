 # https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque
que = deque()
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def BFS(i, j, visit, land, X, Y, column):
    que.append((i, j))
    visit[i][j] = 1
    check = set()
    MAX = 0
    while que:
        x, y = que.popleft()
        check.add(y)
        MAX += 1
        for a, b in dire:
            tx, ty = x + a, y + b
            if not (0 <= tx < X and 0 <= ty < Y): continue
            if not land[tx][ty] or visit[tx][ty]: continue
            visit[tx][ty] = 1
            que.append((tx, ty))
    for i in check:
        column[i] += MAX
        
def solution(land):
    answer = 0
    X = len(land)
    Y = len(land[0])
    visit = [[0] * Y for _ in range(X)]
    column = [0] * Y
    for i in range(X):
        for j in range(Y):
            if not visit[i][j] and land[i][j]:
                BFS(i, j, visit, land, X, Y, column)
    return max(column)
