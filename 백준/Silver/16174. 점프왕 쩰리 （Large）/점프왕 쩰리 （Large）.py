n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
visit[0][0] = 1
for i in range(n):
    for j in range(n):
        if not visit[i][j]: continue
        if 0 <= i + graph[i][j] < n and not visit[i + graph[i][j]][j]:
            visit[i + graph[i][j]][j] = 1
        if 0 <= j + graph[i][j] < n and not visit[i][j + graph[i][j]]:
            visit[i][j + graph[i][j]] = 1
if visit[n - 1][n - 1]:
    print("HaruHaru")
else:
    print("Hing")