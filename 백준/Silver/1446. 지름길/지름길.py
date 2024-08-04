n, d = map(int, input().split())
arr = [tuple(map(int ,input().split())) for _ in range(n)]
DP = [i for i in range(10001)]
arr.sort()
for i in range(d + 1):
    if i > 0: DP[i] = min(DP[i], DP[i - 1] + 1)
    for st, ed, cost in arr:
        if i == st and DP[ed] > DP[st] + cost:
            DP[ed] = min(DP[ed], DP[st] + cost)
    
print(DP[d])