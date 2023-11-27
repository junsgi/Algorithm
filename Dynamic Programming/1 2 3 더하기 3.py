#https://www.acmicpc.net/problem/15988
DP = [0] * (1_000_001)
DP[1] = 1
DP[2] = 2
DP[3] = 4
for i in range(4, 1_000_001):
    DP[i] = (DP[i - 3] + DP[i - 2] + DP[i - 1]) % 1_000_000_009
n = int(input())
for _ in range(n):
    print(DP[int(input())])