import sys
input = sys.stdin.readline
def p(node, tree, e):
    if not tree[node]: return 1
    res = 0
    flag = False
    for i in tree[node]:
        if i == e: continue
        flag = True
        res += p(i, tree, e)
    if not flag: return 1    
    return res
n = int(input().strip())
arr = tuple(map(int, input().strip().split()))
tree = [[] for _ in range(n)]
e = int(input().strip())
root = -1
for i in range(n):
    if arr[i] == -1: root = i
    else: tree[arr[i]].append(i)
tree[e].clear()
if root == e: print(0)
else : print(p(root, tree, e))