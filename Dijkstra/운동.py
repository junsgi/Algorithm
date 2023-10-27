# https://www.acmicpc.net/problem/1956
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[1e12] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
ans = 1e12
for i in range(1, n + 1):
    ans = min(ans, graph[i][i])
print(-1 if ans == 1e12 else ans)