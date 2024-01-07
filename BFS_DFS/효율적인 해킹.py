import sys
from collections import deque, defaultdict
input = sys.stdin.readline
def BFS(node, check):
    global MAX
    que.clear()
    que.append(node)
    visit[node] = check
    cnt = 0
    while que:
        tnode = que.popleft()
        cnt += 1
        
        for nxt in graph[tnode]:
            if visit[nxt] == check : continue
            visit[nxt] = check
            que.append(nxt)
    MAX = max(cnt, MAX)
    return cnt

v, e = map(int, input().split())
graph = defaultdict(list)
que = deque()
MAX = 0
for _ in range(e):
    a, b = map(int, input().split())
    graph[b].append(a)
visit = [0] * (v + 1)
result = []
for i in range(1, v + 1):
    if len(graph[i]) != 0:
        res = BFS(i, i)
        result.append((res, i))
result.reverse()
while result:
    tmp = result.pop()
    if tmp[0] == MAX:
        print(tmp[1], end = ' ')