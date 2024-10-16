def solution(diffs, times, limit):
    answer = 0
    l, r = 1, 1_000_000_000_000_000
    while l <= r:
        level = (l + r) // 2
        sec = times[0]
        for i in range(1, len(times)):
            if diffs[i] <= level:
                sec += times[i]
            else:
                sec += (diffs[i] - level) * (times[i - 1] + times[i]) + times[i]
            
            if sec >= limit:
                break
        if sec <= limit:
            r = level - 1
        else:
            l = level + 1
    return l