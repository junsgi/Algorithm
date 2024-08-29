n, m = map(int, input().split())
DP = [[0 for _ in range(m + 1)]]
for _ in range(n):
    DP.append([0] + list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        DP[i][j] += max(DP[i - 1][j], DP[i][j - 1])
print(DP[n][m])