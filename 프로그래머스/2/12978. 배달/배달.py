def solution(N, road, K):
    answer = 0
    graph = [[0x7fffffff] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1): graph[i][i] = 0
    
    for a, b, c in road:
        graph[a][b] = graph[b][a] = min(c, min(graph[a][b], graph[b][a]))
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for i in graph[1]:
        if i <= K: answer += 1
    return answer