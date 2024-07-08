def solution(a, b):
    answer = 0
    res = a % 2 + b % 2
    if res == 2: return a * a + b * b
    elif res == 1: return (a + b) * 2
    return abs(a - b)