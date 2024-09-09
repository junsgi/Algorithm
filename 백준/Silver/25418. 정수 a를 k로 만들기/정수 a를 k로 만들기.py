n, m = map(int, input().split())
DP = [999999] * (m + 1)
DP[n] = 0
for i in range(n, m + 1):
    if i + 1 <= m:
        DP[i + 1] = min(DP[i + 1], DP[i] + 1)
    if i * 2 <= m:
        DP[i * 2] = min(DP[i * 2], DP[i] + 1)
print(DP[m])