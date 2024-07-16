MAX = 0x7fffffff
n, m = map(int, input().split())
graph = [[MAX] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
answer = 0
MIN = 0x7fffffff
for i in range(1, n + 1):
    s = sum(graph[i][1:])
    if MIN > s:
        answer = i
        MIN = s
print(answer)