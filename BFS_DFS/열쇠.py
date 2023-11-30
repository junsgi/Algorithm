# https://www.acmicpc.net/problem/9328
import sys
from collections import deque
input = sys.stdin.readline


dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def BFS(Key, cnt, graph, visit):
    que = deque()
    visit[0][0] = cnt
    que.append((0, 0))
    result = 0
    while que:
        x, y = que.popleft()

        for a, b in dire:
            tx, ty = x + a, y + b
            if not (0 <= tx < len(graph) and 0 <= ty < len(graph[0])): continue
            if visit[tx][ty] == cnt : continue
            if graph[tx][ty] == '*': continue
            visit[tx][ty] = cnt

            if graph[tx][ty] == '.':
                que.append((tx, ty))
            elif 'a' <= graph[tx][ty]: # 열쇠라면
                Key.add(graph[tx][ty])
                graph[tx][ty] = '.'
                que.append((tx, ty))   
            elif 'A' <= graph[tx][ty] and graph[tx][ty].lower() in Key: # 문을 열 수 있으면
                graph[tx][ty] = '.'
                que.append((tx, ty))
            elif graph[tx][ty] == '$':
                result += 1
                graph[tx][ty] = '.'
                que.append((tx, ty))

    return result
        

N = int(input())
for _ in range(N):
    n, m = map(int, input().split())
    visit = [[0] * (m + 2) for _ in range(n + 2)]
    graph = [list('.' * (m + 2))]
    for _ in range(n):
        graph.append(['.'] + list(input().strip()) + ['.'])
    graph.append(list('.' * (m + 2)))
    Key = set()
    for k in input().strip():
        if k == '0' : break
        Key.add(k)
    ans = 0
    cnt = 1
    while True:
        length = len(Key)
        ans += BFS(Key, cnt, graph, visit)
        cnt += 1
        if length == len(Key): break

    print(ans)