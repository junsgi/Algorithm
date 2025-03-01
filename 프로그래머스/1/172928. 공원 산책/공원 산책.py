def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    x, y = -1, -1
    dire = {"N" : (-1, 0), "S" : (1, 0), "W" : (0, -1),"E" : (0, 1)}
    for i in range(n):
        park[i] = list(park[i])
        for j in range(m):
            if park[i][j] == 'S':
                park[i][j] = "O"
                x, y = i, j
    for i in routes:
        comm, cnt = i.split()
        cnt = int(cnt)
        tx, ty = x + dire[comm][0] * cnt, y + dire[comm][1] * cnt
        if not (0 <= tx < n and 0 <= ty < m): continue
        tx, ty = x, y
        hit = False
        for i in range(cnt):
            tx += dire[comm][0]
            ty += dire[comm][1]
            if park[tx][ty] == "X": 
                hit = True
                break
        if not hit:
            x, y = tx, ty
    answer = [x, y]
    return answer