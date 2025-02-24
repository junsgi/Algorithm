def p(depth, idx, tmp, limit):
    if depth == 5:
        return [tmp]
    res = []
    for i in range(idx, limit + 1):
        for j in p(depth + 1, i + 1, tmp + [i], limit):
            res.append(j)
    return res
def solution(n, q, ans):
    answer = 0
    arr = p(0, 1, [], n)
    for a in arr:
        tmp = [0] * len(ans)
        for i in range(len(q)):
            for j in q[i]:
                if j in a:
                    tmp[i] += 1
            if tmp[i] > ans[i]:
                break
        else:
            if tmp == ans:
                answer += 1
    return answer
