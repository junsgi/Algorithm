# https://www.acmicpc.net/problem/7570
n = int(input())
a = list(map(int, input().split()))
DP = [0] * (n + 1)
ans = 0
for i in a:
    DP[i] += DP[i - 1] + 1
    ans = max(ans, DP[i])
print(n - ans)