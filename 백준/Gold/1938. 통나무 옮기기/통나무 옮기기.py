# https://www.acmicpc.net/problem/1938
from collections import deque
n = int(input())
tree = []
graph = []
dire = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for i in range(n):
    graph.append(list(input()))
    for j in range(n):
        if graph[i][j] == 'B':
            tree.append([i, j])

visit = [[[[0] * n for i in range(n)] for _ in range(3)] for __ in range(2)]

que = deque()
temp = []


# 깊이
tree.append(0)

# 세워져있으면 True
if tree[0][1] == tree[1][1]:
    tree.append(True)
else:
    tree.append(False)

for i in range(3):
    visit[tree[-1]][i][tree[i][0]][tree[i][1]] = 1
que.append(tree)


def limit(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def CHECK(T, s):
    x, y = 0, 0
    x2, y2= 0, 0
    if s : 
        x, y = T[0][0] + 1, T[0][1] - 1
        x2, y2 = T[2][0] - 1, T[2][1] + 1
    else:
        x, y = T[0][0] - 1, T[0][1] + 1
        x2, y2 = T[2][0] + 1, T[2][1] - 1
    sx, sy = T[1][0] - 1, T[1][1] - 1
    for i in range(sx, sx + 3):
        for j in range(sy, sy + 3):
            if not limit(i, j) or graph[i][j] == '1':
                return [[]]
    return [[x, y], [T[1][0], T[1][1]], [x2, y2]]
    
    
def VISIT(tree, s):
    cnt = 0
    for i in range(3):
        cnt += visit[s][i][tree[i][0]][tree[i][1]]
    return cnt != 3

ans = 0
while que:
    t = que.popleft()
    tree = [t[0], t[1], t[2]]
    depth = t[3]
    status = t[4]

    if graph[tree[0][0]][tree[0][1]] == 'E' and graph[tree[1][0]][tree[1][1]] == 'E' and graph[tree[2][0]][tree[2][1]] == 'E':
        ans = depth
        break

    for a, b in dire:
        swi = False
        temp = []
        for i in range(3):
            tx, ty = tree[i][0] + a, tree[i][1] + b
            if not limit(tx, ty) or graph[tx][ty] == '1':
                swi = True
                break
            temp.append([tx, ty])

        if not swi and VISIT(temp, status):
            for i in range(3):
                visit[status][i][temp[i][0]][temp[i][1]] = 1
            temp.append(depth + 1)
            temp.append(status)
            que.append(temp)

    temp2 = CHECK(tree, status)
    if temp2[0] and VISIT(temp2, not status):
        for i in range(3):
            visit[not status][i][temp2[i][0]][temp2[i][1]] = 1
        temp2.append(depth + 1)
        temp2.append(not status)
        que.append(temp2)
print(ans)