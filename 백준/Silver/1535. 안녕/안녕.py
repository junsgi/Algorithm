n = int(input())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))
DP = [[0] * (101) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if minus[i - 1] <= j:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - minus[i - 1]] + plus[i - 1])
        else:
            DP[i][j] = DP[i - 1][j]
print(DP[n][99])