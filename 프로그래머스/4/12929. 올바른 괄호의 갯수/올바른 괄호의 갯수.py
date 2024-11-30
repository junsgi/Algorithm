def solution(n):
    DP = [1, 1, 2]
    for i in range(3, 15):
        s = 0
        for j in range(i):
            s += DP[j] * DP[i - j - 1]
        DP.append(s)
    return DP[n]