def solution(arr):
    c = 1
    while c < len(arr): c *= 2
    for _ in range(c - len(arr)): arr.append(0)
    return arr