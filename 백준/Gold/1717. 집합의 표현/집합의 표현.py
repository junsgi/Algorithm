import sys
sys.setrecursionlimit(1_000_001)
input = sys.stdin.readline
def find(x):
    global p
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]
def union(x, y):
    global p
    fx, fy = find(x), find(y)
    if fx == fy: return
    if fx < fy:
        p[fy] = fx
    else:
        p[fx] = fy

n, m = map(int, input().split())
p = [i for i in range(n + 1)]
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")