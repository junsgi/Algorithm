# https://www.acmicpc.net/problem/1799
dire = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

def RANGE(x, y):
    global n
    return 0 <= x < n and 0 <= y < n
def CHECK(x, y):
    x1, y1, z1 = x + dire[0][0], y + dire[0][1], True
    x2, y2, z2 = x + dire[1][0], y + dire[1][1], True
    x3, y3, z3 = x + dire[2][0], y + dire[2][1], True
    x4, y4, z4 = x + dire[3][0], y + dire[3][1], True
    cnt = 4

    while cnt:
        if z1 and RANGE(x1, y1):
            if visit[x1][y1]:
                return False
            x1 += dire[0][0]; y1 += dire[0][1]
        else:
            if z1 :
                cnt -= 1
            z1 = False

        if z2 and RANGE(x2, y2):
            if visit[x2][y2]:
                return False
            x2 += dire[1][0]; y2 += dire[1][1]
        else:
            if z2:
                cnt -= 1
            z2 = False

        if z3 and RANGE(x3, y3):
            if visit[x3][y3]:
                return False
            x3 += dire[2][0]; y3 += dire[2][1]
        else:
            if z3:
                cnt -= 1
            z3 = False

        if z4 and RANGE(x4, y4):
            if visit[x4][y4]:
                return False
            x4 += dire[3][0]; y4 += dire[3][1]
        else:
            if z4:
                cnt -= 1
            z4 = False
    return True
             
def BACK(depth, cnt):
    global ans
    if depth == len(location):
        return
    ans = max(ans, cnt)
    x, y = location[depth][0], location[depth][1]
    if CHECK(x, y): # 선택한다
        visit[x][y] = 1
        BACK(depth + 1, cnt + 1)
        visit[x][y] = 0
    # 안 한다.
    BACK(depth + 1, cnt)
n = int(input())
ans = 0
visit = [[0] * n for _ in range(n)]
location = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            location.append([i, j])
BACK(0, 0)
print(ans)