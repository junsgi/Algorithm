def solution(n):
    answer = [[0] * n for _ in range(n)]
    dire = ((0, 1), (1, 0), (0, -1), (-1, 0))
    cnt = n * n
    x, y, N = 0, 0, 1
    c = 0
    while cnt != 0:
        answer[x][y] = N
        cnt -= 1
        N += 1
        tx, ty = x + dire[c % 4][0], y + dire[c % 4][1]
        if not (0 <= tx < n and 0 <= ty < n) or answer[tx][ty] != 0:
            c += 1
            tx, ty = x + dire[c % 4][0], y + dire[c % 4][1]
            
        x, y = tx, ty
    return answer