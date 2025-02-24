def solution(a, b):
    ref = "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU",  
    m = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = b
    for i in range(1, a):
        d += m[i]
    return ref[d % 7 - 1]