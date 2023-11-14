# https://www.acmicpc.net/problem/2302
DP = [1, 1, 2]
for _ in range(41):
    DP.append(DP[-1] + DP[-2])
n = int(input())
m = int(input())
st = 0
answer = 1
t = 0
for _ in range(m):
    t = int(input())
    answer *= DP[t - st - 1]
    st = t
print(answer * DP[n - t])