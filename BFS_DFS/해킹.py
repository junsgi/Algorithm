# https://www.acmicpc.net/problem/28283
from collections import deque
N, M, X, Y = map(int, input().split())
cost = list(map(int, input().split()))

graph = {i:[] for i in range(1, N + 1)}
que = deque()
result = []
visit = [0] * (N + 1)
for _ in range(M):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

lst = list(map(int, input().split()))
for s in lst:
    que.append([s, 1])
    visit[s] = 1

# 보안 프로그램이 설치된 컴퓨터부터 탐색시작
while que:
    node, depth = que.popleft()
    
    for i in graph[node]:
        if visit[i] == 0:
            visit[i] = depth + 1
            que.append([i, depth + 1])

answer = 0
visit.pop(0)
for i in range(len(visit)):
    if visit[i] == 0 and cost[i] != 0:
        print(-1)
        exit()
        
for i in range(N):
    visit[i] = (visit[i] - 1) * cost[i]
visit.sort(reverse=True)
for i in range(X):
    answer += visit[i]
print(answer)