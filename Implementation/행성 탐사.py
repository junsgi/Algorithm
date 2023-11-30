# https://www.acmicpc.net/problem/5549
# 2차원 누적합으로 풀 수 있는 문제
import sys
input = sys.stdin.readline
def check(x):
    if x == "J": return [1, 0, 0]
    if x == "O": return [0, 1, 0]
    if x == "I": return [0, 0, 1]
n, m = map(int, input().strip().split())
k = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
DP = [[[0] * (m + 1) for _ in range(n + 1)] for __ in range(3)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        t = check(graph[i - 1][j - 1])
        DP[0][i][j] = DP[0][i][j - 1] + DP[0][i - 1][j] - DP[0][i - 1][j - 1] + t[0]
        DP[1][i][j] = DP[1][i][j - 1] + DP[1][i - 1][j] - DP[1][i - 1][j - 1] + t[1]
        DP[2][i][j] = DP[2][i][j - 1] + DP[2][i - 1][j] - DP[2][i - 1][j - 1] + t[2]

for _ in range(k):
    sx, sy, ex, ey = map(int, input().strip().split())
    a = DP[0][ex][ey] - DP[0][ex][sy - 1] - DP[0][sx - 1][ey] + DP[0][sx - 1][sy - 1]
    b = DP[1][ex][ey] - DP[1][ex][sy - 1] - DP[1][sx - 1][ey] + DP[1][sx - 1][sy - 1]
    c = DP[2][ex][ey] - DP[2][ex][sy - 1] - DP[2][sx - 1][ey] + DP[2][sx - 1][sy - 1]
    print(a, b, c)