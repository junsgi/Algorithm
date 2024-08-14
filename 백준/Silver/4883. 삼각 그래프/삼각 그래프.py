cnt = 1
dire = ((0, -1), (-1, -1), (-1, 0), (-1, 1))
while n := int(input()):
    graph = tuple(tuple(map(int, input().split())) for _ in range(n))
    DP = [[0x7fffffff] * 3 for _ in range(n)]
    DP[0][0] = 0x7fffffff
    DP[0][1] = graph[0][1]
    DP[0][2] = graph[0][1] + graph[0][2]
    for i in range(1, n):
        for j in range(3):
            for a, b in dire:
                tx, ty = i + a, j + b
                if not (0 <= tx < n and 0 <= ty < 3) : continue
                DP[i][j] = min(DP[i][j], DP[tx][ty] + graph[i][j])
    print(f"{cnt}. {DP[n - 1][1]}")
    cnt += 1
