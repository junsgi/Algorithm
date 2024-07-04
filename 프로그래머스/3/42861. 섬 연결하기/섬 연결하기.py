def find(node, arr):
    if node == arr[node]:
        return node
    arr[node] = find(arr[node], arr)
    return arr[node]

def union(x, y, arr):
    fx, fy = find(x, arr), find(y, arr)
    if fx == fy :
        return False
    if fx < fy:
        arr[fy] = fx
    else:
        arr[fx] = fy
    return True
        
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    P = [i for i in range(n + 1)]
    for st, ed, cost in costs:
        if union(st, ed, P):
            answer += cost
    return answer