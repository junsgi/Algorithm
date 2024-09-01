from heapq import heappush, heappop
from copy import deepcopy
dire = ((-1, 0), (1, 0), (0, -1), (0, 1), )
count = 0
visit = [[0] * 4 for _ in range(4)] 

def inRange(x, y):
    return 0 <= x < 4 and 0 <= y < 4
def onCtrl(x, y, d, board):
    tx, ty = x + dire[d][0], y + dire[d][1]
    while inRange(tx, ty) and board[tx][ty] == 0:
        tx += dire[d][0]
        ty += dire[d][1]
    if not inRange(tx, ty):
        tx -= dire[d][0]
        ty -= dire[d][1]
    return tx, ty
def findCards(x, y, board, target = -1):
    global count, visit
    dist = [[0x7fffffff] * 4 for _ in range(4)]
    if target == -1 and board[x][y] != 0: return [(x, y, 0)]
    heap = []
    heappush(heap, (0, x, y))
    visit[x][y] = (count := count + 1)
    res = []
    while heap:
        depth, nx, ny = heappop(heap)

        for i in range(4):
            tx, ty = onCtrl(nx, ny, i, board)
            if visit[tx][ty] != count:
                visit[tx][ty] = count
                heappush(heap, (depth + 1, tx, ty))

            if board[tx][ty] == target:
                return tx, ty, depth + 1
            if target == -1 and board[tx][ty] != 0 and dist[tx][ty] > depth + 1:
                dist[tx][ty] = depth + 1
                res.append((tx, ty, depth + 1))

            tx, ty = nx + dire[i][0], ny + dire[i][1]
            if not inRange(tx, ty): continue
            if visit[tx][ty] == count: continue
            if board[tx][ty] == target or target == -1 and board[tx][ty] != 0 and dist[tx][ty] > depth + 1:
                dist[tx][ty] = depth + 1
                res.append((tx, ty, depth + 1))
            visit[tx][ty] = count
            heappush(heap, (depth + 1, tx, ty))
    return res


def BFS(board, r, c):
    global count, visit
    heap = []
    heappush(heap, (0, r, c, board))
    MAX = 0x7fffffff
    while heap:
        depth, x, y, nBoard = heappop(heap)
        fcs = findCards(x, y, nBoard)
        if len(fcs) == 0:
            return depth
        else:
            for targetx, targety, cnt in fcs:
                tBoard = deepcopy(nBoard)
                target, tBoard[targetx][targety] = tBoard[targetx][targety], 0
                tx, ty, tc = findCards(targetx, targety, tBoard, target = target)
                tBoard[tx][ty] = 0
                heappush(heap, (depth + cnt + tc + 2, tx, ty, tBoard))
def solution(board, r, c):
    return BFS(board, r, c)