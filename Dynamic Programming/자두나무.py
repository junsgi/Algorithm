# https://www.acmicpc.net/problem/2240 
T, W = map(int, input().split())
plum = [0]
for _ in range(T):
    plum.append(int(input()))
DP = [[[0] * 3 for _ in range(W + 2)] for __ in range(T + 1)]
# DP[time][change cnt][tree loc] = 자두 개수
"""
큐에 넣는 경우의 수
1. 각 초마다 위치를 바꾼다
"""
if plum[1] == 1 :
    DP[1][1][1] = 1
else:
    DP[1][2][2] = 1

for t in range(2, T + 1):
    before = plum[t]

    for w in range(1, W + 2):
        if before == 1: # 1번 나무에서 자두가 떨어졌다면
            # 가만히 있거나 2번에서 1번으로 오는 경우
            DP[t][w][1] = max(DP[t - 1][w][1], DP[t - 1][w - 1][2]) + 1
            DP[t][w][2] = max(DP[t - 1][w - 1][1], DP[t - 1][w][2])
        else:
            DP[t][w][1] = max(DP[t - 1][w][1], DP[t - 1][w - 1][2])
            DP[t][w][2] = max(DP[t - 1][w - 1][1], DP[t - 1][w][2]) + 1
ans = 0
for i in range(T + 1):
    for j in range(1, W + 2):
        ans = max(ans, max(DP[i][j]))
print(ans)