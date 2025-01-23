def solution(r1, r2):
    answer = 0
    p1, p2 = r1, r2
    n1, n2 = 0, 0
    for x in range(r2 + 1):
        while x * x + p2 * p2 > r2 * r2:
            p2 -= 1
        n2 += p2 + 1
    for x in range(r1 + 1):
        while x * x + p1 * p1 > r1 * r1:
            p1 -= 1
        if x * x + p1 * p1 == r1 * r1:
            n2 += 1
        n1 += p1 + 1
    answer = (n2 - n1) * 4
    answer -= (r2 - r1 + 1) * 4
    return answer
