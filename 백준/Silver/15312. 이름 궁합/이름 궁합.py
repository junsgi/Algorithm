cost = 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1
s1 = input()
s2 = input()
DP = [[0] * i for i in range(len(s1) + len(s2), 1, -1)]
idx = 0
for i in s1:
    DP[0][idx] = cost[ord(i) - 65]
    idx += 2
idx = 1
for i in s2:
    DP[0][idx] = cost[ord(i) - 65]
    idx += 2

for i in range(1, len(DP)):
    for j in range(len(DP[i])):
        DP[i][j] = (DP[i - 1][j] + DP[i - 1][j + 1]) % 10
print(f"{DP[-1][0]}{DP[-1][1]}")