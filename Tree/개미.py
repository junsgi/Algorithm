import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def BFS():
    que.append(1)
    visit[1] = 1

    while que:
        node = que.popleft()
        for v, c in graph[node]:
            if visit[v] : continue
            visit[v] = 1
            DP[0][v] = node
            WEIGHT[0][v] = c
            que.append(v)
            

n = int(input())
value = [0]
graph = defaultdict(list)
que = deque()
DP = [[0] * (n + 1) for _ in range(20)]
WEIGHT = [[0] * (n + 1) for _ in range(20)]
visit = [0] * (n + 1)
cnt = 0
for _ in range(n):
    value.append(int(input()))
for _ in range(n - 1):
    st, ed, c = map(int, input().strip().split())
    graph[st].append([ed, c])
    graph[ed].append([st, c])
temp = 1
while temp <= n:
    cnt += 1
    temp *= 2

BFS()
# 희소배열 생성
for i in range(1, cnt + 1):
    for j in range(1, n + 1):
        DP[i][j] = DP[i - 1][DP[i - 1][j]]
        WEIGHT[i][j] = WEIGHT[i - 1][j] + WEIGHT[i - 1][DP[i - 1][j]]

for i in range(1, n + 1):
    user = i
    for j in range(cnt, -1, -1):
        if WEIGHT[j][user] <= value[i]:
            value[i] -= WEIGHT[j][user]
            user = DP[j][user]
    if not user: 
        user += 1
    print(user)