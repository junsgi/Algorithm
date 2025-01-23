def solution(n):
    a, b, c = 0, 1, 0
    m = 1234567
    for _ in range(n):
        c = a % m + b % m
        a = b % m
        b = c % m
        
    return c % m