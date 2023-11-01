# https://www.acmicpc.net/problem/2302
n = int(input())
m = int(input())
check = [0] * (n + 1)
DP = [0] * (n + 1)
for _ in range(m):
    check[int(input())] = 1
if check[1] == 0:
    DP[1] = 2

for i in range(2, n + 1):
    if check[i]:continue
    else:
        if i + 1 <= n and check[i + 1] != 1:
            DP[i] = DP[i - 1] + 1
        else:
            DP[i] = DP[i - 1]
print(sum(DP))
print(DP)