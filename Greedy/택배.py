# https://www.acmicpc.net/problem/8980
n, MAX = map(int, input().split())
m = int(input())
box = [0] * (n + 1)
arr = [list(map(int, input().split())) for _ in range(m)]

# 가까운 마을에 빨리 택배를 보내야 하므로 도착지를 기준으로 오름차순 정렬
arr.sort(key = lambda x : x[1])

ans = 0
for st, ed, cost in arr:

    # 도착과 동시에 택배를 내리므로 출발지점 ~ 도착지점 - 1 까지만 탐색
    t = max(box[st:ed])
    MIN = min(MAX - t, cost)
    for i in range(st, ed):
        box[i] += MIN
    ans += MIN
print(ans)