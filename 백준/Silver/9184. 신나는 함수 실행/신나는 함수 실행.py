DP = [[[0] * 21 for _ in range(21)] for __ in range(21)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if 0 <= a <= 20 and 0 <= b <= 20 and 0 <= c <= 20 and DP[a][b][c] != 0:
        return DP[a][b][c]
    if a > 20 or b > 20 or c > 20:
        DP[20][20][20] = w(20, 20, 20)
        return DP[20][20][20]
    elif a < b < c:
        DP[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return DP[a][b][c]
    else:
        DP[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return DP[a][b][c]
    


while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")