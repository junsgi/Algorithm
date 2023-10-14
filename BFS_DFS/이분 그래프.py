# https://www.acmicpc.net/problem/1707
# 이분 그래프 자료구조
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = {}
que = deque()
def BFS(key, visit):
    global ans
    que.clear()
    que.append(key)
    visit[key] = 1

    while que:
        value = que.popleft()
        for v in graph[value]:
            # 방문한 적 없다면
            if visit[v] == 0:
                # 현재 방문 값의 부호가 다르게 표시
                visit[v] = -visit[value]
                que.append(v)
                
                # 방문은 했지만 부호까지 같다면 다른 집합에도 포함되므로 이분 그래프가 아님
            elif visit[v] == visit[value]:
                ans = "NO"
                return


for _ in range(n):
    v, e = map(int, input().split())
    graph.clear()
    ans = "YES"
    check = [0] * (v + 1)
    for __ in range(e):
        st, ed = map(int, input().split())
        check[st] = check[ed] = 1
        if st in graph:
            graph[st].append(ed)
        else:
            graph[st] = [ed]

        if ed in graph:
            graph[ed].append(st)
        else:
            graph[ed] = [st]
    visit = [0] * (v + 1)
    for i in range(1, v + 1):
        if ans == 'NO': break
        # 입력되지 않은 정점이거나 해당 정점을 방문한 적있다면
        if not check[i] or visit[i]: continue
        BFS(i, visit)
    print(ans)
"""
1
6 6
1 3
3 4
4 2
2 5
5 6
6 1
"""