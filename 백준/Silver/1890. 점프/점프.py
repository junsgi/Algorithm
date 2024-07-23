import sys
input = sys.stdin.readline
sys.setrecursionlimit(10010)
def memo(x, y):
    global n, graph, DP
    if not (0 <= x < n and 0 <= y < n): return 0

    if x == n - 1 and y == n - 1:
        return 1
    if graph[x][y] == 0:
        return 0
    if DP[x][y] != -1:
        return DP[x][y]
    t1 = memo(x, y + graph[x][y])
    t2 = memo(x + graph[x][y], y)
    DP[x][y] = t1 + t2
    return DP[x][y]

n = int(input())
graph = [tuple(map(int, input().strip().split())) for _ in range(n)]
DP = [[-1] * n for _ in range(n)]
print(memo(0, 0))