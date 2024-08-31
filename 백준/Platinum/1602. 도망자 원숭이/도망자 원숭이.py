import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
d = list(zip(map(int, input().strip().split()), range(1, n + 1)))
dog = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        dog[i + 1][j + 1] = max(d[i][0], d[j][0])
d = [0] + sorted(d, key = lambda x : x[0])
MAX = 0x7fffffff
graph = [[MAX] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s][e] = graph[e][s] = min(graph[e][s], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] + dog[i][j] > graph[i][d[k][1]] + graph[d[k][1]][j] + max(dog[i][d[k][1]], dog[d[k][1]][j]):
                graph[i][j] = graph[i][d[k][1]] + graph[d[k][1]][j]
                dog[i][j] = max(dog[i][d[k][1]], dog[d[k][1]][j])
for _ in range(q):
    st, ed = map(int, input().split())
    if graph[st][ed] == MAX:
        print(-1)
    else:
        print(graph[st][ed] + dog[st][ed])