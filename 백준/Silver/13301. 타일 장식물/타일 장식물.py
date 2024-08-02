DP = [0] * 81
DP[1] = 1
for i in range(2, 81):
    DP[i] = DP[i - 1] + DP[i - 2]
n = int(input())
print((DP[n] * 2 + DP[n - 1]) * 2)