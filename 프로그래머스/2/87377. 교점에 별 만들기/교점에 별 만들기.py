from math import floor
def get(a, b, e, c, d, f, check):
    if a * d - b * c == 0:
        return -100001 * 100001, -100001 * 100001
    p = a * d - b * c
    x = (b * f - e * d) / p
    y = (e * c - a * f) / p
    res = floor(x), floor(y), 
    if x - floor(x) == 0 and y - floor(y) == 0 and res not in check:
        check.add(res)
        return res
    return -100001 * 100001, -100001 * 100001
def solution(line):
    answer = []
    arr = []
    check = set()
    px, py = 100001 * 100001, 100001 * 100001
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            x, y = get(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2], check)
            if x <= -100001 * 100001: continue
            arr.append((x, y))
            px = min(px, x)
            py = min(py, y)
    mx, my = -100001 * 100001, -100001 * 100001
    px, py = -px, -py
    star = [[0 for _ in range(1002)] for __ in range(1002)]
    for i in range(len(arr)):
        star[arr[i][0] + px][arr[i][1] + py] = 1
        mx = max(mx, arr[i][0] + px)
        my = max(my, arr[i][1] + py)
    for j in range(my, -1, -1):
        res = ""
        for i in range(mx + 1):
            res += "*" if star[i][j] else "."
        answer.append(res)
    return answer