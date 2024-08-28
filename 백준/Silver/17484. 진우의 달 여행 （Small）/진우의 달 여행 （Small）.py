def p(x, y, prev, value):
    global n, m, arr, DP, dire, answer
    if x == n - 1:
        answer = min(answer, value)
        return
    if answer < value:
        return
    for i in range(3):
        tx, ty = x + 1, y + dire[i]
        if not (0 <= ty < m): continue
        if i == prev: continue
        p(tx, ty, i, value + arr[tx][ty])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dire = (-1, 0, 1)
answer = 9999
for i in range(m):
    p(0, i, -1, arr[0][i])
print(answer)