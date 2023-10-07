# https://www.acmicpc.net/problem/1080
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
target = [list(input()) for _ in range(n)]

if n < 3 or m < 3 :
    print(-1)
    exit()

def change(x, y, matrix):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = '1' if matrix[i][j] == '0' else '0'
ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        swi = False
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if matrix[x][y] != target[x][y]:
                    swi = True
                    ans += 1
                    change(i, j, matrix)
                    break
            if swi:
                break
print("mat")
for mat in matrix:
    print(mat)
print("tar")

for t in target:
    print(t)
print()
for i in range(n):
    for j in range(m):
        if matrix[i][j] != target[i][j]:
            print(-1)
            exit()
print(ans)