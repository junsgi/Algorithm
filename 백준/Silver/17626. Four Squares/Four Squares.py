n = int(input())
DP = [i for i in range(n + 1)]
for i in range(2, n + 1):
    for j in range(1, i):
        if j * j > i: break
        DP[i] = min(DP[i], DP[i - j * j] + 1)
print(DP[n])