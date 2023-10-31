# https://www.acmicpc.net/problem/17265
n = int(input())
arr = [list(input().split()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
def check(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def oper(a, b, c):
    if b == '+' : return a + c
    if b == '-' : return a - c
    return a * c

def DFS(x, y, ord, ort):
    global MIN, MAX, n
    if x == n - 1 and y == n - 1 :
        MIN = min(MIN, ord)
        MAX = max(MAX, ord)
        return
    if check(x, y + 1) and not visit[x][y + 1]:
        visit[x][y + 1] = 1
        if arr[x][y + 1].isdigit():
            DFS(x, y + 1, oper(ord, ort, int(arr[x][y + 1])), ort)
        else:
            DFS(x, y + 1, ord, arr[x][y + 1])
        visit[x][y + 1] = 0

    if check(x + 1, y) and not visit[x + 1][y]:
        visit[x + 1][y] = 1
        if arr[x + 1][y].isdigit():
            DFS(x + 1, y, oper(ord, ort, int(arr[x + 1][y])), ort)
        else:
            DFS(x + 1, y, ord, arr[x + 1][y])
        visit[x + 1][y] = 0

MIN = 0x7fffffff
MAX = -MIN
visit[0][0] = 1
DFS(0, 0, int(arr[0][0]), "")
print(MAX, MIN)