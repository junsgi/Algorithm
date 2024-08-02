def p(x, y, cx, cy):
    global DP
    if x == cx and y == cy:
        return 1
    if DP[x][y] != 0:
        return DP[x][y]
    if x + 1 <= n:
        DP[x][y] += p(x + 1, y, cx, cy)
    if y + 1 <= m:
        DP[x][y] += p(x, y + 1, cx, cy)
    return DP[x][y]
n, m, k = map(int, input().split())
DP = [[0] * (m + 1) for _ in range(n + 1)]
a, b = (k - 1) // m + 1, (k - 1) % m + 1
if k > 0:
    print(p(1, 1, a, b) * p(a, b, n, m))
else:
    print(p(1, 1, n, m))