def solution(cookie):
    answer = 0
    N = len(cookie)
    DP = [0]
    for c in cookie:
        DP.append(DP[-1] + c)
    print(DP)
    k = 1
    while k <= N:
        f, s = k - 1, k
        while f >= 1 and s <= N:
            F, S = DP[k - 1] - DP[f - 1], DP[s] - DP[k - 1]
            if F < S:
                f -= 1
            elif F > S:
                s += 1
            else:
                answer = max(answer, F)
                f -= 1
                s += 1
        k += 1
    return answer