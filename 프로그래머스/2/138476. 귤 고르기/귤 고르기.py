def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    arr = list(sorted(dic.items(), key = lambda x : -x[1]))
    for n, c in arr:
        answer += 1
        k -= c
        if k <= 0:
            break
    return answer