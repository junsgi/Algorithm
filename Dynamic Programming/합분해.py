# https://www.acmicpc.net/problem/2225
n, m = map(int, input().split())
DP = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    DP[i][0] = 1
    for j in range(1, n + 1):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % 1_000_000_000
print(DP[m][n])