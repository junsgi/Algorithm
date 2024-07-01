def solution(n,a,b):
    answer = 0
    cnt = 0
    t = 1
    while t < n :
        t *= 2
        cnt += 1
    a = 2 ** cnt + a - 1
    b = 2 ** cnt + b - 1
    
    while a != b:
        a //= 2
        b //= 2
        answer += 1

    return answer