def solution(dirs):
    answer = 0
    x, y = 5, 5
    visit = [[[[0] * 11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    dire = {
        "U" : (-1, 0),
        "D" : (1, 0),
        "L" : (0, -1),
        "R" : (0, 1)
    }
    for d in dirs:
        tx, ty = x + dire[d][0], y + dire[d][1]
        if not (0 <= tx < 11 and 0 <= ty < 11): continue
        if not visit[x][y][tx][ty]: answer += 1
        visit[x][y][tx][ty] = 1
        visit[tx][ty][x][y] = 1
        x, y = tx, ty
    return answer