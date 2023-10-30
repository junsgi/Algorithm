#https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque

def getLoc(x, y, w, d, g):
    while True:
        tx = x + d[w][0]
        ty = y + d[w][1]
        if not (0 <= tx < len(g) and 0 <= ty < len(g[tx])) or g[tx][ty] == 'D':
            return (x, y)
        x = tx
        y = ty

def solution(board):
    dire = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    sx, sy = -1, -1
    ex, ey = -1, -1
    que = deque()
    visit = [[0] * len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board)):
        board[i] = list(board[i])
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                sx, sy = i, j
            if board[i][j] == 'G':
                ex, ey = i, j
                
    que.append((sx, sy, 0))
    visit[sx][sy] = 1
    
    while que:
        x, y, depth = que.popleft()
        
        if x == ex and y == ey:
            return depth
        for i in range(4):
            tx, ty = getLoc(x, y, i, dire, board)
            if visit[tx][ty]: continue
            visit[tx][ty] = 1
            que.append((tx, ty, depth + 1))
    answer = 0
    return -1