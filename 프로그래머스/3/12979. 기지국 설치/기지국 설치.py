def solution(n, stations, w):
    answer = 0
    start = 1
    for i in stations:
        end = i - w - 1
        if end < 0 or start > end:
            start = i + w + 1
            continue
        answer += (end - start + 1) // (w * 2 + 1)
        if (end - start + 1) % (w * 2 + 1):
            answer += 1
        start = i + w + 1
    if stations[-1] != n:
        answer += (n - start + 1) // (w * 2 + 1)
        if (n - start + 1) % (w * 2 + 1):
            answer += 1
    return answer