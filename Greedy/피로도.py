#https://www.acmicpc.net/problem/22864
T, W, H, L = map(int, input().split())
cur = 0
ans = 0
for i in range(1, 25):
    if cur + T <= L:
        ans += W
        cur += T
    else:
        cur -= H
        if cur - H < 0 :
            cur = 0
print(ans)