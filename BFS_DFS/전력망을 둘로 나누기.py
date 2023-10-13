# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def solution(n, wires):
    cnt = [0, 0]
    def search(key, visit, c):
        cnt[c] += 1
        if key not in tree:
            cnt[c] += 1
            return
        for k in tree[key]:
            if check[key][k] or check[k][key] or visit[k]: continue
            visit[k] = 1
            search(k, visit, c)
    answer = 0x7fffffff
    tree = {}
    check = [[0] * (n + 1) for _ in range(n + 1)]
    for st, ed in wires:
        if st in tree:
            tree[st].append(ed)
        else:
            tree[st] = [ed]
        
        if ed in tree:
            tree[ed].append(st)
        else:
            tree[ed] = [st]

    for st, ed in wires:
        check[st][ed] = 1
        check[ed][st] = 1
        visit = [0] * (n + 1)
        j = 0
        for i in tree.keys():
            if not visit[i]:
                visit[i] = 1
                search(i, visit, j)
                visit[i] = 0
                j += 1
                if j >= 2:break
        if sum(cnt) == n:
            answer = min(answer, abs(cnt[0] - cnt[1]))
        cnt[0] = cnt[1] = 0
        check[st][ed] = 0
        check[ed][st] = 0
            
    return answer
