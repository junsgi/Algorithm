n = int(input())
graph = tuple(tuple(map(int, input().split())) for _ in range(n))
DP = [[0] * n for _ in range(n)]
for i in range(n): DP[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == k or k == j: continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                exit()
            
            if graph[i][j] == graph[i][k] + graph[k][j]:
                DP[i][j] = 1
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if DP[i][j] == 0: answer += graph[i][j]
print(answer)