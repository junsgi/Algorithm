def solution(n, times):
    answer = 0
    times.sort(reverse = True)
    1_000_000_000_000_000_000
    le = 1
    ri = 1_000_000_000_000_000_000
    while le <= ri:
        mid = (le + ri) // 2
        temp = n
        if temp <= 0:
            ri = mid - 1
        else:
            for time in times:
                temp -= mid // time
                if temp <= 0:
                    ri = mid - 1
                    break
            else:
                le = mid + 1
    return le