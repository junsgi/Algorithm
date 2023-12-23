# https://www.acmicpc.net/problem/17182
def DFS(depth, value, node):
    global n, m, answer
    if depth == n:
        answer = min(value, answer)
        return
    for i in range(n):
        if visit[i] : continue
        visit[i] = 1
        DFS(depth + 1, value + graph[node][i], i)
        visit[i] = 0
    
n, m = map(int, input().split())
answer = 0x7fffffff
graph = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
visit = [0] * (n + 1)
DFS(0, 0, m)
print(answer)