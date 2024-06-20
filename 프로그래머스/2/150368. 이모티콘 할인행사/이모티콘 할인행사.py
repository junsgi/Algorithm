def rec(depth, res, users, emoticons):
    if depth == len(emoticons):
        temp = [0, 0]
        for disc, limit in users:
            S = 0
            for i in range(len(res)):
                if res[i] < disc: continue
                S += int(emoticons[i] - emoticons[i] * (res[i] / 100))
                
            if S >= limit:
                temp[0] += 1
            else:
                temp[1] += S
        return temp
    
    result = [0, 0]
    for i in range(10, 41, 10):
        CNT, SUM = rec(depth + 1, res + [i], users, emoticons)
        if (result[0] < CNT) or (result[0] == CNT and result[1] < SUM):
            result[0] = CNT
            result[1] = SUM
    return result

def solution(users, emoticons):
    return rec(0, [], users, emoticons)