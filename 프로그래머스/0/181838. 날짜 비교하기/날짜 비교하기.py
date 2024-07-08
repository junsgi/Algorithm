def solution(date1, date2):
    d1 = date1[0] * 10000 + date1[1] * 100 + date1[2]
    d2 = date2[0] * 10000 + date2[1] * 100 + date2[2]
    if d1 < d2: return 1
    return 0