def solution(n):
    answer = 0
    while n:
        answer = answer * 10 + n % 3
        n //= 3
    k = 1
    while answer:
        n += k * (answer % 10)
        k *= 3
        answer //= 10
    return n