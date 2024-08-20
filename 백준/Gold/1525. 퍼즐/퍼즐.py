from collections import deque, defaultdict
dire = ((-1, 0), (1, 0), (0, -1), (0, 1))
def getCode(graph):
    return "".join(graph)
def move(d, graph:list):
    loc = graph.index("0")
    x, y = loc // 3, loc % 3
    tx, ty = x + dire[d][0], y + dire[d][1]
    if not (0 <= tx < 3 and 0 <= ty < 3): return graph
    graph[x * 3 + y], graph[tx * 3 + ty] = graph[tx * 3 + ty], graph[x * 3 + y]
    return graph

path = defaultdict(int)
def p(node): # 역추적
    global path
    if node == -1:
        return
    p(path[node])
    for i in range(9):
        if i > 0 and i % 3 == 0: print()
        print(node[i], end = ' ')
    print()
    print()

def solution(graph):
    global path
    que = deque()
    check = set()
    check.add(getCode(graph))
    que.append((graph, 0))
    path[getCode(graph)] = -1
    s = "123456780"
    while que:
        g, d = que.popleft()
        if getCode(g) == s:
            # p(getCode(g)) 역추적
            return d
        for i in range(4):
            tg = move(i, g[:])
            th = getCode(tg)
            if th in check: continue
            path[th] = getCode(g)
            check.add(th)
            que.append((tg, d + 1))
    return -1
graph = []
for _ in range(3):
    for i in input().split():
        graph.append(i)
print(solution(graph))
