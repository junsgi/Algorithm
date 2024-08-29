x, y, w = map(int, input().split())
dp = [[1] * i for i in range(1, 61)]
for i in range(2, len(dp)):
    for j in range(1, len(dp[i]) - 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

answer = 0
c = 1
for i in range(x - 1, x - 1 + w):
    for j in range(c):
        answer += dp[i][j + (y - 1)]
    c += 1
print(answer)