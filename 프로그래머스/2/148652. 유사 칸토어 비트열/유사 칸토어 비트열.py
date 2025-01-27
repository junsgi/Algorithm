import sys
sys.setrecursionlimit(50)
def solution(n, l, r):
    def p(k, depth, left, right):
        nonlocal n, l, r
        
        if right < l or r < left:
            return 0
        if depth == n:
            return k
        res = 0
        g = (right - left + 1) // 5
        if k == 1:
            res += p(1, depth + 1, left, left + g - 1)
            res += p(1, depth + 1, left + g, left + g * 2 - 1)
            res += p(0, depth + 1, left + g * 2, left + g * 3 - 1)
            res += p(1, depth + 1, left + g * 3, left + g * 4 - 1)
            res += p(1, depth + 1, left + g * 4, left + g * 5 - 1)
        else:
            res += p(0, depth + 1, left, left + g - 1)
            res += p(0, depth + 1, left + g, left + g * 2 - 1)
            res += p(0, depth + 1, left + g * 2, left + g * 3 - 1)
            res += p(0, depth + 1, left + g * 3, left + g * 4 - 1)
            res += p(0, depth + 1, left + g * 4, left + g * 5 - 1)
        return res
    return p(1, 0, 1, 5 ** n)