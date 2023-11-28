# https://www.acmicpc.net/problem/1865
import sys
input = sys.stdin.readline
def BellmanFord(n, edge):
    visit = [1e12] * (n + 1)
    visit[1] = 0
    for v in range(1, n + 1):
        for st, ed, cost in edge:
            if visit[ed] > visit[st] + cost:
                visit[ed] = visit[st] + cost
    
    for st, ed, cost in edge:
        if visit[ed] > visit[st] + cost:
            return True
    return False

N = int(input())
for _ in range(N):
    n, m, w = map(int, input().split())
    edge = []
    for __ in range(m):
        a, b, c = map(int, input().split())
        edge.append([a, b, c])
        edge.append([b, a, c])
    for __ in range(w):
        a, b, c = map(int, input().split())
        edge.append([a, b, -c])

    if BellmanFord(n, edge):
        print("YES")
    else:
        print("NO")