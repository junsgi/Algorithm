def p(depth, idx, limit, value, arr):
    if depth == limit:
        return value + " "
    result = ""
    for i in range(idx, len(arr)):
        res = p(depth + 1, i + 1, limit, value + arr[i], arr)
        result += res
    return result

def solution(orders, course):
    answer = []
    for i in range(len(orders)): orders[i] = sorted(orders[i])
    graph = [[] for _ in range(11)]
    for word in orders:
        for c in course:
            if len(word) < c: continue
            comb = p(0, 0, c, "", word).split()
            res = set()
            for t in comb: res.add(t)
            graph[c].append(res)
    arr = []
    for c in course:
        if not graph[c]: continue
        dic = {}
        for i in range(len(graph[c])):
            for w in graph[c][i]:
                if w in dic : dic[w] += 1
                else: dic[w] = 1
        
        arr = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
        MAX = arr[0][1]
        if MAX < 2 : continue
        answer.append(arr[0][0])
        for i in range(1, len(arr)):
            if arr[i][1] == MAX:
                answer.append(arr[i][0])
            else:
                break
            
    return sorted(answer)
