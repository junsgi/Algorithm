# https://www.acmicpc.net/problem/17265
n = int(input())
arr = [list(input().split()) for _ in range(n)]
DP = [[0] * n for _ in range(n)]
def check(x, y):
    global n
    return not (0 <= x < n and 0 <= y < n)

def oper(a, b, c):
    if b == '+' : return a + c
    if b == '-' : return a - c
    return a * c

def DFS(x, y, ord, ort, value):
    global MIN, MAX

    if check(x, y + 1):
        if arr[x][y + 1].isdigit():
            if ord:
                DFS(x, y + 1, 0, "", value + oper(ord, ort, arr[x][y + 1]))
            else:
                DFS(x, y + 1, arr[x][y + 1], ort, value)
        else:
            DFS(x, y + 1, ord, arr[x][y + 1], value)

    if check(x + 1, y):
        if arr[x + 1][y].isdigit():
            if ord:
                DFS(x + 1, y, 0, "", value + oper(ord, ort, arr[x + 1][y]))
            else:
                DFS(x + 1, y, arr[x + 1][y], ort, value)
        else:
            DFS(x + 1, y, ord, arr[x + 1][y], value)


MIN = 0x7fffffff
MAX = 0

DFS(0, 0)
print(MAX, MIN, 0, "", 0)