def p(n, c):
    if n == 1: return c
    if n % 2 == 0: return p(n // 2, c + 1)
    else: return p(n - 1, c)
def solution(num_list):
    answer = 0
    for i in num_list:
        answer += p(i, 0)
    return answer