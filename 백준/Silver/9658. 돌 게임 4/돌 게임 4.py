n = int(input())
DP = [0] * 1001
DP[2] = 1
DP[4] = 1
DP[5] = 1
for i in range(5, 1001):
    if DP[i - 1] == 1 and DP[i - 3] == 1 and DP[i - 4] == 1:
        DP[i] = 0
    else:
        DP[i] = 1
print("SK" if DP[n] == 1 else "CY")