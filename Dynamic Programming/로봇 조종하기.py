# https://www.acmicpc.net/problem/2169
n, m = map(int, input().split())
init = list(map(int, input().split()))
DP = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, m + 1):
    DP[1][i] = init[i - 1] + DP[1][i - 1]
goLeft = [-0x7fffffff] * (m + 2)
goRight = [-0x7fffffff] * (m + 2)
for i in range(2, n + 1):
    arr = list(map(int, input().split()))

    for j in range(1, m + 1):
        goRight[j] = arr[j - 1] + max(goRight[j - 1], DP[i - 1][j])
        goLeft[m - j + 1] = arr[m - j] + max(goLeft[m - j + 2], DP[i - 1][m - j + 1])
    
    for j in range(1, m + 1):
        DP[i][j] = max(goLeft[j], goRight[j])

print(DP[n][m])