

def check(loc, board):
    return 0 <= loc[0] < len(board) and 0 <= loc[1] < len(board[0]) and board[loc[0]][loc[1]] == 1

def is_finished(x, y, board):
    for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if check((x + a, y + b), board):
            return False
    return True
def move(me, you, board):
    if is_finished(me[0], me[1], board):
        return False, 0
    
    if me[0] == you[0] and me[1] == you[1]:
        return True, 1
    
    canWin = False
    max_cnt = 0
    min_cnt = 0x7fffffff
    for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        td = me[0] + a, me[1] + b
        if not (0 <= td[0] < len(board) and 0 <= td[1] < len(board[0])): continue
        if board[td[0]][td[1]] == 0: continue
        board[me[0]][me[1]] = 0
        winner, cnt = move(you, td, board)
        board[me[0]][me[1]] = 1
        if not winner: 
            canWin = True
            min_cnt = min(min_cnt, cnt)
        else:
            max_cnt = max(max_cnt, cnt)
    return canWin, (min_cnt if canWin else max_cnt) + 1
    

def solution(board, aloc, bloc):
    return move(aloc, bloc, board)[1]
