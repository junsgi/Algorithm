# https://www.acmicpc.net/problem/1826
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.append([float("inf"), float("inf")])
target, cOil = map(int, input().split())
arr.sort(key = lambda x : x[0])
cur = 0
nxt = cur + cOil
mxOil, mxY = -1, -1
ans = 0
idx = 0
# 현재 위치 갈 수 있는 거리 안에 가장 멀리 갈 수 있는 주유소 선택
# 현재위치에서 가장 멀고, 가장 많이 주유할 수 있는 곳
# 주유소 위치 - 현재 위치 + 주유소 주유량
while True:
    dis, getOil = arr[idx]
    if dis <= nxt:
        d = (dis + getOil) + (cOil - (dis - cur))
        if mxOil < d:
            mxOil, mxY = d, dis
        idx += 1
    else:
        ans += 1
        cur = mxY
        mxOil = mxY = -1
