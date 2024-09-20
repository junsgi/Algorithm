import sys
input = sys.stdin.readline
n, m = map(int, input().split())
MAX = 0x7fffffff
graph = [[MAX] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j : continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    s, e = map(int, input().split())
    if graph[s][e] == MAX and graph[e][s] == MAX: print(0)
    elif graph[s][e] != MAX : print(-1)
    else: print(1)