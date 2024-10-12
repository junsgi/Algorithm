from collections import deque
def check(l, r, s):
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def solution(s):
    answer = 1
    for i in range(1, len(s)):
        for j in range(i):
            if answer < (i - j + 1) and check(j, i, s):
                answer = max(answer, i - j + 1)
    return answer