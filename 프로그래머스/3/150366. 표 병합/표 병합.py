def key(a, b):
    return a * 50 + b
def find(node, p):
    if node == p[node][0]:
        return node
    p[node][0] = find(p[node][0], p)
    return p[node][0]
def union(x, y, p):
    fx, fy = find(x, p), find(y, p)
    if fx == fy: return
    v1, v2 = p[fx][1], p[fy][1]
    value = ""
    if v2: value = v2
    if v1: value = v1
    if fx < fy:
        p[fy][0] = fx
        p[fx][1] = value
    else:
        p[fx][0] = fy
        p[fy][1] = value
def update(p, case1 = None, case2 = None):
    if case1:
        loc, value = case1
        loc = find(loc, p)
        p[loc][1] = value
    else:
        before, after = case2
        for i in range(len(p)):
            if p[i][1] == before:
                p[i][1] = after
    return 
def unmerge(k, p):
    pk = find(k, p)
    value = p[pk][1]
    tmp = []
    for i in range(len(p)):
        if find(p[i][0], p) == pk:
            tmp.append(i)
    for t in tmp:
        p[t][0] = t
        p[t][1] = ""
    p[pk][0] = pk
    p[pk][1] = ""
    p[k][0] = k
    p[k][1] = value
            
def solution(commands):
    answer = []
    p = [[i, ""] for i in range(2500)]
    for comm in commands:
        c = comm.split()
        if c[0] == "UPDATE" and len(c) == 4:
            k = key(int(c[1]) - 1, int(c[2]) - 1)
            update(p, case1 = [k, c[3]])
        elif c[0] == "UPDATE":
            update(p, case2 = [c[1], c[2]])
        elif c[0] == "MERGE":
            union(key(int(c[1]) - 1, int(c[2]) - 1), key(int(c[3]) - 1, int(c[4]) - 1), p)
        elif c[0] == "UNMERGE":
            unmerge(key(int(c[1]) - 1, int(c[2]) - 1), p)
        else:
            k = find(key(int(c[1]) - 1, int(c[2]) - 1), p)
            if p[k][1]:
                answer.append(p[k][1])
            else:
                answer.append("EMPTY")
        # print(" ".join(map(str, c)))
        # for i in range(16):
        #     print(p[i], end = ' ')
        #     if (i + 1) % 4 == 0: print()
        # print()
    return answer