# https://www.acmicpc.net/problem/1941
import sys
input = sys.stdin.readline
queen = [input().strip() for _ in range(5)]
check = [[0] * 5 for _ in range(5)]
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0
visit = [[0] * 5 for _ in range(5)]
Y, S = 0, 0
def SEARCH(i, j):
    global visit, Y, S
    if Y >= 4: return
    if queen[i][j] == 'Y':
        Y += 1
    else:
        S += 1
    
    for a, b in dire:
        tx, ty = i + a, j + b
        if not (0 <= tx < 5 and 0 <= ty < 5): continue
        if check[tx][ty] == 0 or visit[tx][ty] == 1: continue

        visit[tx][ty] = 1
        SEARCH(tx, ty)
        
    
def BACK(x, y, depth):
    global ans, visit, Y, S
    if depth == 7:
        Y = S = 0
        visit = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if check[i][j]:
                    visit[i][j] = 1
                    SEARCH(i, j)
                    if Y < 4 and Y + S == 7:
                        ans += 1
                    return
    if y == 5:
        x += 1
        y = 0
    if x == 5: return

    check[x][y] = 1
    BACK(x, y + 1, depth + 1)

    check[x][y] = 0
    BACK(x, y + 1, depth)
BACK(0, 0, 0)
print(ans)