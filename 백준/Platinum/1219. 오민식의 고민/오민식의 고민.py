MIN = -0x80000000
n, st, ed, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]
money = list(map(int, input().split()))
cost = [MIN] * n
cost[st] = money[st]
hit = 0
for i in range(n + 101):
    for x, y, c in arr:
        if cost[x] == MIN: continue
        elif cost[x] == -MIN: cost[y] = -MIN
        elif cost[y] < cost[x] + (money[y] - c):
            cost[y] = cost[x] + (money[y] - c)
            if i >= n - 1:
                cost[y] = -MIN
                if y == ed:
                    hit = 1
                    break
    if hit: break
if cost[ed] == -MIN: print("Gee")
elif cost[ed] == MIN: print("gg")
else: print(cost[ed])
