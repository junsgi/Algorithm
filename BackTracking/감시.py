import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
a = []
cctv = 0
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 1번 CCTV : 상 또는 하 또는 좌 또는 우 방향으로만 감시
# 2번 CCTV : 상하 또는 좌우 방향으로만 감시
# 3번 CCTV : 상우, 하우, 하좌, 상좌 방향으로만 감시
# 4번 CCTV : 상좌우, 상하우, 하좌우, 상하좌 방향으로만 감시
# 5번 CCTV : 4방향 동시에 감시
check = [0,
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
    [[0, 1, 2, 3]]
]
loc = []
for i in range(n):
    a.append(list(map(int, input().strip().split())))
    for j in range(m):
        if a[i][j] != 6 and a[i][j] != 0:
            cctv += 1
            loc.append((i, j, a[i][j]))
            a[i][j] = 0

def MOVE(x, y, key : bool, d : int):
    global n, m
    while True:
        if not ( 0 <= x < n and 0 <= y < m) or a[x][y] == 6: break

        if key:
            a[x][y] -= 1
        else:
            a[x][y] += 1

        x += dire[d][0]
        y += dire[d][1]


ans = 0x7fffffff
def back(depth):
    global cctv, ans

    if depth == cctv:
        t1 = 0
        for row in a:
            t1 += row.count(0)
            if t1 >= ans: return # 구했던 개수보다 많다면 back
        ans = t1
        if ans == 0: # 0보다 더 작아질 수 없기 때문에 출력 후 종료
            print(0)
            exit()
        return
    
    x = loc[depth][0]
    y = loc[depth][1]

    for i in check[loc[depth][2]]:

        for j in i: # 현재 CCTV의 번호에 맞게 감시중인 곳 표시
            MOVE(x, y, True, j)
            
        back(depth + 1)

        for j in i: # 지우기
            MOVE(x, y, False, j)
back(0)
print(ans)