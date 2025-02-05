def solution(n):
    answer = 0
    a = [0] * 10
    while n:
        a[n % 10] += 1
        n //= 10
    for i in range(9, -1, -1):
        while a[i]:
            a[i] -= 1
            answer = answer * 10 + i
    return answer