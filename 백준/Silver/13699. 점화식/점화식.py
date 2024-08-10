DP = [0] * 36
DP[0] = 1
DP[1] = 1
for i in range(2, 36):
    for j in range(i):
        DP[i] += DP[j] * DP[i - j - 1]
print(DP[int(input())])