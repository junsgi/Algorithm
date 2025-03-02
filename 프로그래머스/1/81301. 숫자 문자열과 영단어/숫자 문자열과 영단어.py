def solution(s):
    answer = 0
    ck = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    idx = 0
    t = ''
    for i in s:
        if i.isdigit():
            answer = answer * 10 + int(i)
        else:
            t += i
            if t in ck:
                answer = answer * 10 + ck[t]
                t = ''
    return answer