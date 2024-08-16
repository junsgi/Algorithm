n, m, t, d = map(int, input().split())
dire = ((-1, 0), (1, 0), (0, -1), (0, 1))
graph = [[0] * m for _ in range(n)]
MAX = 0x7fffffff
DP = [[MAX] * (n * m) for _ in range(n * m)]
for i in range(n * m): DP[i][i] = 0
getHeight = lambda x : ord(x) - 65 if x <= 'Z' else ord(x) - 97 + 26
for i in range(n):
    h = input()
    for j in range(m):
        graph[i][j] = getHeight(h[j])
for i in range(n):
    for j in range(m):
        N = i * m + j
        
        for a, b in dire:
            ti, tj = i + a, j + b
            M = ti * m + tj
            if not (0 <= ti < n and 0 <= tj < m): continue
            if abs(graph[i][j] - graph[ti][tj]) > t: continue
            if graph[i][j] < graph[ti][tj]:
                DP[N][M] = (graph[ti][tj] - graph[i][j]) * (graph[ti][tj] - graph[i][j])
            else:
                DP[N][M] = 1
for k in range(n * m):
    for i in range(n * m):
        for j in range(n * m):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
answer = 0
for i in range(n * m):
    if DP[0][i] + DP[i][0] <= d and answer < graph[i // m][i % m]:
        answer = graph[i // m][i % m]
print(answer)