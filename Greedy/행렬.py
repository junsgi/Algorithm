# https://www.acmicpc.net/problem/1080
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
target = [list(input()) for _ in range(n)]

if n < 3 or m < 3 :
    if matrix == target:
        print(0)
    else:
        print(-1)
    exit()

def change(x, y, matrix):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = '1' if matrix[i][j] == '0' else '0'
ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if matrix[i][j] != target[i][j]:
            ans += 1
            change(i, j, matrix)
if matrix == target:
    print(ans)
else:
    print(-1)