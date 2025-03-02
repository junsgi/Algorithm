def solution(keymap, targets):
    answer = []
    ck = dict()
    for k in keymap:
        for i in range(len(k)):
            if k[i] not in ck:
                ck[k[i]] = i + 1
            else:
                ck[k[i]] = min(ck[k[i]], i + 1)
    for target in targets:
        res = 0
        for t in target:
            if t not in ck:
                res = -1
                break
            else:
                res += ck[t]
        answer.append(res)
    return answer