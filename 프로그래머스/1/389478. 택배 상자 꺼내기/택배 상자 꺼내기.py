def solution(n, w, num):
    answer=  0
    c = n // w
    box = [[0] * w for _ in range(c + 1)]
    cnt = 0
    x, y, k = 0, 0, 1
    i, j = -1, -1
    for _ in range(c + 1):
        if cnt + 1 > n:break
        for __ in range(w):
            if cnt + 1 > n:break
            box[x][y] = (cnt := cnt + 1)
            if box[x][y] == num:
                i, j = x, y
            y += k
        y += -k
        k = -k
        x += 1
    while i < c + 1 and box[i][j] != 0:
        answer += 1
        i += 1
    return answer