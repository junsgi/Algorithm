# https://www.acmicpc.net/problem/1208
n, target = map(int, input().split())
arr = list(map(int, input().split()))
A = []
B = []
check = set()
answer = 0
def BACK(idx, end, res, arr):
    global answer, n, target
    if idx == end:
        return
    arr.append(res)
    BACK(idx + 1, end, res + arr[idx], arr)
    BACK(idx + 1, end, res, arr)

BACK(0, n // 2, 0, A)
BACK(n // 2, n, 0, B)

