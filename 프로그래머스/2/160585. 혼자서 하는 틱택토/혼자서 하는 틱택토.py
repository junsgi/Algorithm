def isDone(graph):
    for i in range(3):
        for j in range(3):
            row, col, left, right = 0, 0, 0, 0
            for k in range(3):
                if j - k >= 0:
                    row += graph[i][j - k]
                if i - k >= 0:
                    col += graph[i - k][j]
                if i - k >= 0 and j - k >= 0:
                    left += graph[i - k][j - k]
                if i - k >= 0 and j + k < 3:
                    right += graph[i - k][j + k]
            case1 = row == -3 or row == 3
            case2 = col == -3 or col == 3
            case3 = left == -3 or left == 3
            case4 = right == -3 or right == 3
            if case1 or case2 or case3 or case4:
                return 1
    return 0
def gtos(g):
    res = ""
    for i in range(9):
        t = g[i // 3][i % 3]
        if t == 0: 
            res += "."
        elif t == 1:
            res += "O"
        else:
            res += "X"
    return res
def solution(board):
    answer = -1
    board = "".join(board)
    graph = [[0] * 3 for _ in range(3)]
    o, x = [], []
    def p(turn, co, cx):
        nonlocal board, o, x, graph
        if turn == len(o) + len(x):
            if board == gtos(graph):
                return 1
            return 0
        if isDone(graph):
            return 0
        if turn & 1 == 0:
            for i in range(len(o)):
                if co & (1 << i): continue
                graph[o[i][0]][o[i][1]] = 1
                res = p(turn + 1, co | (1 << i), cx)
                if res: return res
                graph[o[i][0]][o[i][1]] = 0
        else:
            for i in range(len(x)):
                if cx & (1 << i): continue
                graph[x[i][0]][x[i][1]] = -1
                res = p(turn + 1, co, cx | (1 << i))
                if res: return res
                graph[o[i][0]][o[i][1]] = 0
        return 0
    for i in range(9):
        if board[i] == "O":
            o.append((i // 3, i % 3))
        if board[i] == 'X':
            x.append((i // 3, i % 3))
    if len(o) - len(x) != 1 and len(o) - len(x) != 0:
        return 0
    return p(0, 0, 0)