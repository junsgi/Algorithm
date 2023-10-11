# https://school.programmers.co.kr/learn/courses/30/lessons/64064
import re
def solution(user_id, banned_id):
    answer = []
    dout = {}
    for b in range(len(banned_id)):
        dout[b] = []
    for idx, fword in enumerate(banned_id):
        mch = "^"
        for w in fword:
            if "A" <= w <= 'Z' or 'A' <= w or w.isdigit():
                mch += w
            else:
                mch += '.'
        mch += '$'
        for u in user_id:
            ban = re.match(mch, u)
            if ban:
                dout[idx].append(u)

    def req(depth, values):
        if depth == len(dout):
            if len(values) != len(dout):
                return
            if not answer:
                answer.append(values)
            else:
                for sets in answer:
                    if not (sets - values):
                        return
                answer.append(values)
            return            
        for i in range(len(dout[depth])):
            req(depth + 1, values | {dout[depth][i]})

    req(0, set())
    return len(answer)



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))