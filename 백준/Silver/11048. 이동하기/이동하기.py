import sys
input = sys.stdin.readline
sys.setrecursionlimit(1500)
def memo(x, y):
    global n, m, graph, DP
    if not (0 <= x < n and 0 <= y < m): return 0

    if x == n - 1 and y == m - 1:
        return graph[x][y]
    if DP[x][y] != -1:
        return DP[x][y]
    t1 = graph[x][y] + memo(x + 1, y)
    t2 = graph[x][y] + memo(x, y + 1)
    t3 = graph[x][y] + memo(x + 1, y + 1)
    DP[x][y] = max(t1, t2, t3)
    return DP[x][y]

n, m = map(int, input().split())
graph = [tuple(map(int, input().strip().split())) for _ in range(n)]
DP = [[-1] * m for _ in range(n)]
print(memo(0, 0))