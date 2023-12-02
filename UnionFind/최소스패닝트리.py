# https://www.acmicpc.net/problem/1197
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x : x[2])
visit = [i for i in range(n + 1)]
def find(node):
    if node == visit[node]:
        return node
    return find(visit[node])

def union(n1, n2, t1, t2):

    if n1 < n2:
        visit[t2] = t1
    else:
        visit[t1] = t2
ans = 0
for st, ed, cost in arr:
    s, e = find(st), find(ed)
    if s != e:
        union(st, ed, s, e)
        ans += cost
print(ans)
