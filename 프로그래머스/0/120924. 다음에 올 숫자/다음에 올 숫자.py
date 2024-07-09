def solution(common):
    answer = 0
    diff1 = common[1] - common[0]
    diff2 = common[2] - common[1]
    if diff1 != diff2:
        d = diff2 // diff1
        answer = common[-1] * d
    else:
        answer = common[-1] + diff1
    return answer

