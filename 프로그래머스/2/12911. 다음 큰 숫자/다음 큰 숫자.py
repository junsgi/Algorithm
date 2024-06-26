def solution(n):
    c = bin(n).count("1")
    t = n
    cnt = 0
    while c != cnt:
        t += 1
        cnt = bin(t).count("1")
    return t
        
