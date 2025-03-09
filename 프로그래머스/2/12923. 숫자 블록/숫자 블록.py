def f(n):
    if n == 1: return 0
    res = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i <= 10_000_000:
            res = max(res, i)
        if n % i == 0 and n // i <= 10_000_000:
            res = max(res, n // i)
    return res
def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(f(i))
    return answer
