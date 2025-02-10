def solution(scores):
    answer = 1
    a, b = scores[0]
    c = a + b
    scores.sort(key = lambda x : (-x[0], x[1]))
    m = 0
    for i in scores:
        if a < i[0] and b < i[1]:
            return -1
        if m <= i[1]:
            if c < i[0] + i[1]:
                answer += 1
            m = i[1]
    return answer