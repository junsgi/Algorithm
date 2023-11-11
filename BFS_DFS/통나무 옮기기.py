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

def Turn(tre, s):
    global n
    x, y = 0, 0
    
    if s :
        x = tre[0][1] - 1
    else:
        x = tre[0][0] - 1
    y = x
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if not (0 <= i < n and 0 <= j < n) or graph[i][j] == '1':
                return False
    cnt = 0
    if s:
        cnt += visit[not status][0][tre[0][0] + 1][tre[0][1] - 1]
        cnt += visit[not status][2][tre[2][0] - 1][tre[2][1] + 1]
    else:
        cnt += visit[not status][0][tre[0][0] - 1][tre[0][1] + 1]
        cnt += visit[not status][2][tre[2][0] + 1][tre[2][1] - 1]

    cnt += visit[not status][1][tre[1][0]][tre[1][1]]
    return cnt != 3


def Check(n, i, tre, status):
    s = 0
    for j in range(3):
        tx, ty = tre[j][0] + dire[i][0], tre[j][1] + dire[i][1]
        if not (0 <= tx < n and 0 <= ty < n) or graph[tx][ty] == '1':
            return True
        s += visit[status][j][tx][ty]
    return s == 3

while que:
    t = que.popleft()
    print(t)
    tre = [t[0], t[1], t[2]]
    depth = t[3]
    status = t[4]

    if graph[tre[0][0]][tre[0][1]] == 'E' and graph[tre[1][0]][tre[1][1]] == 'E' and graph[tre[2][0]][tre[2][1]] == 'E':
        print(depth)
        break


    # Turn
    if Turn(tre, status):
        temp = []
        for i in tre: temp.append(i)
        k = 1
        for i in range(2):
            if status:
                temp[i // 1][i] += k
            else:
                temp[i // 2 * 2][i % 2] += -k
            k = -k
        if status:
            visit[not status][0][tre[0][0] + 1][tre[0][1] - 1] = 1
            visit[not status][2][tre[2][0] - 1][tre[2][1] + 1] = 1
        else:
            visit[not status][0][tre[0][0] - 1][tre[0][1] + 1] = 1
            visit[not status][2][tre[2][0] + 1][tre[2][1] - 1] = 1

        visit[not status][1][tre[1][0]][tre[1][1]] = 1
        que.append([*temp, depth + 1, not status])


    # 상하좌우
    for i in range(4):

        if Check(n, i, tre, status): continue
        temp.clear()
        for j in range(3):
            tx, ty = tre[j][0] + dire[i][0], tre[j][1] + dire[i][1]
            temp.append([tx, ty])
            visit[status][j][tx][ty] = 1
        que.append([*temp, depth + 1, status])



"""
(1, 0), (2, 0), (3, 0)
[n번째 통나무위치][x위치][y위치]
"""