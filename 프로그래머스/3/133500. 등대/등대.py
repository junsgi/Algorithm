from collections import defaultdict
import sys
sys.setrecursionlimit(100_001)
def get(node, tree, visit): # return 자식이 등대를 켰는지 안 켰는지, 등대 수
    
    isLeaf = True
    on = False
    answer = 0
    for tnode in tree[node]:
        if visit[tnode]: continue
        isLeaf = False
        visit[tnode] = 1
        a, b = get(tnode, tree, visit)
        answer += b
        if not a: on = True # 만약 자식이 등대를 안 켰다면
    if isLeaf: return False, 0
    return on, answer + (1 if on else 0)
def solution(n, lighthouse):
    tree = defaultdict(list)
    for s, e in lighthouse:
        tree[s].append(e)
        tree[e].append(s)
    visit = [0] * (n + 1)
    visit[1] = 1
    on, answer = get(1, tree, visit)
    return answer