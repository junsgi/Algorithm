from math import ceil
def stoi(s):
    x, y = map(int, s.split(":"))
    return x * 60 + y
def solution(fees, records):
    answer = []
    dic = {}
    result = {}
    기본_시간, 기본_요금, 단위_시간, 단위_요금 = fees
    for i in records:
        t, n, c = i.split()
        t = stoi(t)
        if n not in dic: 
            dic[n] = -1
            result[n] = 0
        if c == "IN":
            dic[n] = t
        else:
            result[n] += t - dic[n]
            dic[n] = -1
    end = stoi("23:59")
    for n, c in dic.items():
        if c != -1:
            result[n] += end - c
    for n, c in sorted(result.items(), key = lambda x : x[0]):
        if c <= 기본_시간:
            answer.append(기본_요금)
        else:
            answer.append(기본_요금 + ceil((c - 기본_시간) / 단위_시간) * 단위_요금)
    return answer