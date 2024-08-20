from collections import defaultdict, deque
n = int(input())
origin = [0] * (n + 1)
cost = [0] * (n + 1)
check = [0] * (n + 1)
visit = [0] * (n + 1)
graph = defaultdict(list)
for i in range(1, n + 1):
    arr = tuple(map(int, input().split()))
    origin[i] = arr[0]
    cost[i] = arr[0]
    check[i] += len(arr) - 2
    for j in range(1, len(arr) - 1):
        graph[i].append(arr[j])
        graph[arr[j]].append(i)
que = deque()
for i in range(1, n + 1):
    if check[i] == 0:
        que.append(i)
        visit[i] = 1
while que:
    node = que.popleft()

    for tnode in graph[node]:
        if visit[tnode]: continue
        check[tnode] -= 1
        cost[tnode] = max(cost[tnode], cost[node] + origin[tnode])
        if check[tnode] == 0:
            visit[tnode] = 1
            que.append(tnode)
for i in cost[1:]:
    print(i)