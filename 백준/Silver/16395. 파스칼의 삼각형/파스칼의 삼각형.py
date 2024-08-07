DP = [[1] * (i + 1) for i in range(31)]
for i in range(2, 30):
    for j in range(1, i):
        DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j]
n, k = map(int, input().split())
print(DP[n - 1][k - 1])