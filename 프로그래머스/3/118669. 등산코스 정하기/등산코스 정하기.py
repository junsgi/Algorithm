from collections import defaultdict
def up(idx, heap):
    if idx // 2 <= 0:
        return
    if heap[idx][1] < heap[idx // 2][1]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        up(idx // 2, heap)
def down(idx, heap):
    child = idx * 2
    if child >= len(heap):
        return
    if child + 1 < len(heap) and heap[child][1] > heap[child + 1][1]:
        child += 1
    if heap[idx][1] > heap[child][1]:
        heap[idx], heap[child] = heap[child], heap[idx]
        down(child, heap)
def solution(n, paths, gates, summits):
    answer = [0x7fffffff, 0x7fffffff]
    gate = set(gates)
    summit = set(summits)
    graph = defaultdict(list)
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))
    cost = [0x7fffffff] * (n + 1)
    for g in gates:
        heap = [None, (g, 0)]
        cost[g] = 0
        while len(heap) != 1:
            node, depth = heap[1]
            heap[1] = heap[-1]
            heap.pop()
            down(1, heap)
            if node in summit: continue
            if cost[node] < depth: continue
            for a, b in graph[node]:
                if a in gate: continue
                if cost[a] <= max(depth, b): continue
                cost[a] = max(depth, b)
                heap.append((a, max(depth, b)))
                up(len(heap) - 1, heap)
    for s in summits:
        if cost[s] < answer[1] or cost[s] == answer[1] and s < answer[0]:
            answer = [s, cost[s]]
    return answer
