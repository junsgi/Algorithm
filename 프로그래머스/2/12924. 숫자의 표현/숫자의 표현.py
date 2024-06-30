import math
def solution(n):
    answer = 1
    p1 = 1
    p2 = 2
    while p1 != p2 and p2 != n:
        LEN = p2 - p1 + 1
        S = LEN / 2 * (p1 + p2)
        if S < n:
            p2 += 1
        else:
            if S == n: answer += 1
            p1 += 1
    return answer