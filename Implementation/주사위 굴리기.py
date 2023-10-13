# https://www.acmicpc.net/problem/14499
N, M, dx, dy, com = map(int, input().split())
grp = [list(map(int, input().split())) for _ in range(N)]
com = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0] 

direction = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]

mv = [0, 
[0, 4, 2, 1, 6, 5, 3], # 동
[0, 3, 2, 6, 1, 5, 4], # 서
[0, 5, 1, 3, 4, 6, 2], # 북
[0, 2, 6, 3, 4, 1, 5], # 남
]
for c in com:
    tx, ty = dx + direction[c][0], dy + direction[c][1]
    if not (0 <= tx < N and 0 <= ty < M): 
        continue
    if grp[dx][dy] == 0:
        grp[dx][dy] = dice[1]
    else:
        dice[1], grp[dx][dy] = grp[dx][dy], 0
    dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[mv[c][1]], dice[mv[c][2]], dice[mv[c][3]], dice[mv[c][4]], dice[mv[c][5]], dice[mv[c][6]]
    dx, dy = tx, ty
    print(dice[6])
