# https://www.acmicpc.net/problem10844
n = int(input())
DP = [[0] * (11) for _ in range( n + 1)]
DP[0][0] = 1
for i in range(10):
    DP[1][i] = 1
for i in range(2, n + 1):
    DP[i][0] = DP[i - 1][1]
    DP[i][9] = DP[i - 1][8]
    for j in range(1, 9):
        DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % 1_000_000_000
print(sum(DP[n][1:]) % 1_000_000_000)