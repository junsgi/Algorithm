import sys
input = sys.stdin.readline
def draw(x, y):
    global MAX
    area = graph[x][y]
    vr = [0, 0]
    hr = [0, 0]
    vx = x + 1
    hy = y + 1
    v = True
    h = True
    while v or h:
        if v and 0 <= vx < n:
            if not graph[vx][y]: vr[1] += 1
            elif graph[vx][y] != area:
                vr[0] = graph[vx][y]
                if vr[1] < 2 : vr[1] = MAX
                v = False
            else: v = False
            vx += 1
        else:
            v = False
        
        if h and 0 <= hy < m:
            if not graph[x][hy] : hr[1] += 1
            elif graph[x][hy] != area:
                hr[0] = graph[x][hy]
                if hr[1] < 2 : hr[1] = MAX
                h = False
            else: h = False
            hy += 1
        else:
            h = False
    if vr[1] <= 1 or not vr[0]: vr[1] = MAX
    if hr[1] <= 1 or not hr[0]: hr[1] = MAX
    return vr, hr
        
def DFS(x, y, area):
    global n, m
    if not (0 <= x < n and 0 <= y < m): return
    if visit[x][y] : return
    if not graph[x][y] : return
    visit[x][y] = 1
    graph[x][y] = area
    DFS(x + 1, y, area)
    DFS(x - 1, y, area)
    DFS(x, y + 1, area)
    DFS(x, y - 1, area)

def prim():
    global MAX, nodeLen, ans
    node = 1
    min = MAX
    tnode = -1
    freq[1] = 1
    for i in range(1, nodeLen + 1):
        cost[i] = MAP[1][i]
        if not freq[i] and min > cost[i]:
            min = cost[i]
            node = i
    
    for i in range(1, nodeLen):
        if node == -1:
            ans = -1
            return
        min = MAX; ans += cost[node]; freq[node] = 1 ; tnode = -1

        for j in range(1, nodeLen + 1):
            if node != j and not freq[j]:

                if cost[j] > MAP[node][j]:
                    cost[j] = MAP[node][j]
                
                if min > cost[j]:
                    min = cost[j]
                    tnode = j
        node = tnode


MAX = 0x7fffffff
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
freq = [0] * 101
cost = [0] * 101
MAP = [[0] * 101 for _ in range(101)]
ans = 0
area = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visit[i][j]:
            DFS(i, j, area)
            area += 1

nodeLen = area - 1
for i in range(1, nodeLen + 1):
    for j in range(1, nodeLen + 1):
        if i != j:
            MAP[i][j] = MAX


for i in range(n):
    for j in range(m):
        if graph[i][j]:
            res = draw(i, j)
            if MAP[graph[i][j]][res[0][0]] > res[0][1]:
                MAP[graph[i][j]][res[0][0]] = MAP[res[0][0]][graph[i][j]] = res[0][1]
            
            if MAP[graph[i][j]][res[1][0]] > res[1][1]:
                MAP[graph[i][j]][res[1][0]] = MAP[res[1][0]][graph[i][j]] = res[1][1]
            
prim()
print(-1 if ans == 0 else ans)            