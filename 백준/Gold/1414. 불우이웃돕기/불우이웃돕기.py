def get(i, j):
    global graph
    if 'A' <= graph[i][j] <= 'Z':
        return ord(graph[i][j]) - 38
    elif 'a' <= graph[i][j]:
        return ord(graph[i][j]) - 96
    else:
        return 0
def find(node):
    global p
    if node == p[node]:return node
    p[node] = find(p[node])
    return p[node]

def union(x, y, value):
    global p, c
    fx, fy = find(x), find(y)
    if fx == fy: 
        return
    if fx < fy:
        p[fy] = fx
        c[fx] += value
    else:
        p[fx] = fy
        c[fy] += value

n = int(input())
p = [i for i in range(n)]
c = [0] * n
graph = [list(input()) for _ in range(n)]
arr = []
total = 0
for i in range(n):
    for j in range(n):
        total += get(i, j)
        if i != j and graph[i][j] != '0':
            arr.append((i, j, get(i, j)))
            arr.append((j, i, get(i, j)))
arr.sort(key = lambda x : x[2])
for x, y, v in arr:
    union(x, y, v)
for i in range(1, n):
    if find(i - 1) != find(i):
        print(-1)
        break
else: 
    print(total - sum(c))