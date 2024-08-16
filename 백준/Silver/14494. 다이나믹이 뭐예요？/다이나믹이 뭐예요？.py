n, m = map(int, input().split())
DP = [[0] * (m + 1) for _ in range(n + 1)]
DP[0][0] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        DP[i][j] = (DP[i][j - 1] + DP[i - 1][j - 1] + DP[i - 1][j]) % 1_000_000_007
print(DP[n][m])