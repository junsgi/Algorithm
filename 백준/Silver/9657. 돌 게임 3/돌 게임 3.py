n = int(input())
DP = [0] * 1001
DP[1] = 1
DP[3] = 1
DP[4] = 1
for i in range(5, 1001):
    if DP[i - 1] == 0 or DP[i - 3] == 0 or DP[i - 4] == 0:
        DP[i] = 1
    else:
        DP[i] = 0
print("SK" if DP[n] == 1 else "CY")