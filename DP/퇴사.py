import sys
input = sys.stdin.readline
n = int(input().strip())
a = [0]
DP = [0] * (n + 2)
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n, 0, -1):
    if i + a[i][0] <= n + 1:
        DP[i] = max(DP[i + 1], a[i][1] + DP[i + a[i][0]])
    else:
        DP[i] = DP[i + 1]
print(DP[1])