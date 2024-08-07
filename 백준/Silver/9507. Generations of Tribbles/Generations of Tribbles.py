DP = [1] * 70
DP[2] = 2
DP[3] = 4
for i in range(4, 70):
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3] + DP[i - 4]
for _ in range(int(input())):
    print(DP[int(input())])