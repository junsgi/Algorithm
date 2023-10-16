# https://www.acmicpc.net/problem/1915
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if a[i][j]:
            a[i][j] = min(a[i-1][j-1], a[i-1][j], a[i][j-1]) + 1
ans = 0
for i in a:
    ans = max(ans, max(i))
print(ans ** 2)