# https://www.acmicpc.net/problem/16724
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
def DFS(x, y,  depth, vis):
    global n, m
    if not (0 <= x < n and 0 <= y < m) : return
    if visit[x][y] != -1 and visit[x][y] == vis:
        return 1
    if visit[x][y] != -1 and visit[x][y] != vis: # 미리 만들어 놓은 구역에 들어왔다면
        return 0
    
    visit[x][y] = vis
    if graph[x][y] == 'U':
        return DFS(x - 1, y, depth + 1, vis)
    elif graph[x][y] == 'D':
        return DFS(x + 1, y, depth + 1, vis)
    elif graph[x][y] == 'L':
        return DFS(x, y - 1, depth + 1, vis)
    elif graph[x][y] == 'R':
        return DFS(x, y + 1, depth + 1, vis)
ans = 0
cnt = 1
for i in range(n):
    for j in range(m):
        if visit[i][j] == -1:
            ans += DFS(i, j, 0, cnt)
            cnt += 1
print(ans)