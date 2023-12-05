# https://www.acmicpc.net/problem/1806
n, m = map(int, input().split())
DP = [0]
for value in list(map(int, input().split())):
    DP.append(DP[-1] + value)
left = 0
right = 1
ans = 1e12
while left <= right <= n:
    value = DP[right] - DP[left]
    if left == right or value < m:
        right += 1
    else:
        ans = min(ans, right - left)
        left += 1
print(0 if ans == 1e12 else ans)
