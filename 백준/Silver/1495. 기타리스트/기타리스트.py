import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
arr = tuple(map(int, input().split()))
DP = [[0] * (m + 1) for _ in range(n + 1)]
DP[0][s] = 1
for i in range(1, n + 1):
    for j in range(m + 1):
        if not DP[i - 1][j]:
            continue
        if j + arr[i - 1] <= m:
            DP[i][j + arr[i - 1]] = 1
        if j - arr[i - 1] >= 0:
            DP[i][j - arr[i - 1]] = 1

answer = -1
for i in range(m, -1, -1):
    if DP[n][i]:
        answer = i
        break
print(answer)