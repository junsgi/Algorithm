import sys
from collections import defaultdict, deque
input = sys.stdin.readline
def BFS(node):
    global n, tree
    que = deque()
    que.append((node, 0))
    visit = [0] * (n + 1)
    visit[node] = 1
    result = 0, 0
    while que:
        node, depth = que.popleft()
        if result[1] < depth:
            result = node, depth
        for tnode, cost in tree[node]:
            if visit[tnode] : continue
            visit[tnode] = 1
            que.append((tnode, depth + cost))

    return result

n = int(input().strip())
tree = defaultdict(list)
for _ in range(n):
    T = tuple(map(int, input().strip().split()))
    for i in range(1, len(T) - 2, 2):
        tree[T[0]].append((T[i], T[i + 1]))
node, _ = BFS(1)
_, answer = BFS(node)
print(answer)