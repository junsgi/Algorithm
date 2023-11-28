# https://www.acmicpc.net/problem/1647
import sys
input = sys.stdin.readline

def find(x): # x노드의 부모를 찾는다.
    if check[x] == x:
        return x
    return find(check[x])

def union(n1, n2): # 두 노드의 부모가 서로 다르다는 조건에만 실행되는 함수
    t1 = find(n1)
    t2 = find(n2)

    if n1 < n2:
        check[t2] = t1 # 작은 것이 기준이 되므로 n2의 부모노드는 n1입니다.
    else:
        check[t1] = t2

n, m = map(int, input().split())
check = [i for i in range(n + 1)]
edge = []
for _ in range(m):
    st, ed, cost = map(int, input().split())
    edge.append([st, ed, cost])
edge.sort(key=lambda x : x[2])
ans = 0
sub = 0
for node1, node2, cost in edge:
    if find(node1) != find(node2): # 부모가 다르다면 
        union(node1, node2) # 간선 연결
        ans += cost
        sub = max(sub, cost)
print(ans - sub)