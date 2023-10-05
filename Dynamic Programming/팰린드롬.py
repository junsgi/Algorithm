# https://www.acmicpc.net/problem/10942
import sys
input = sys.stdin.readline
n = int(input())
a = [0]
a.extend(list(map(int, input().split())))
DP = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    DP[i][i] = 1

for i in range(1, n):
    if a[i] == a[i + 1]:
        DP[i][i + 1] = 1

for i in range(3, n + 1):
    for j in range(1, n - i + 2):
        if a[j] == a[j + i - 1] and DP[j + 1][j + i - 2] != 0:
            DP[j][j + i - 1] = 1
    
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(DP[x][y])