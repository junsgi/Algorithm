# https://www.acmicpc.net/problem/16437
"""
1. 늑대는 음수로 양은 양수로
2. 문제와 반대로 역방향으로 그래프 구현
3. 후위 탐색으로 각 서브 트리마다 양을 최대한 모은다.
4. 서브트리의 루트가 늑대라면 늑대 수 + 자식 노드들의 결과가 음수일 때 0으로 처리
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(123460)
def DFS(node):
    if node not in graph or not graph[node]: 
        return 0
    
    result = 0
    for nx, co in graph[node]:
        cost = DFS(nx)
        if cost + co < 0: # 양을 아무리 모아도 늑대가 많다면 0으로 설정
            cost = 0
        else: 
            cost += co
        result += cost

    return result

n = int(input())
graph = {}
for i in range(2, n + 1):
    s, c, d = list(input().split())
    c = int(c); d = int(d)
    if s != 'S': c = -c
    if d not in graph:
        graph[d] = []
    graph[d].append([i, c])

print(DFS(1))