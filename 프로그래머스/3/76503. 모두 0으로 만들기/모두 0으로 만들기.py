from collections import defaultdict
import sys
sys.setrecursionlimit(300_001)
cost = None
def p(node, tree, visit):
    global cost
    answer = 0
    isLeaf = True
    for tnode in tree[node]:
        if visit[tnode]: continue
        isLeaf = False
        visit[tnode] = 1
        cnt, ans = p(tnode, tree, visit)
        answer += ans
        cost[node] += cnt
    t, cost[node] = cost[node], 0
    if isLeaf:
        return t, abs(t)
    else:
        return t, answer + abs(t)
    
    
def solution(a, edges):
    if sum(a): return -1
    global cost
    cost = a
    tree = defaultdict(list)
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    visit = [0] * len(a)
    visit[0] = 1
    _, answer = p(0, tree, visit)
    return answer 