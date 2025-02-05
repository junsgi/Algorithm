def solution(n):
    if n & 1: return 0
    DP = [0] * 5001
    DP[2] = 3
    DP[4] = 11
    for i in range(6, n + 1, 2):
        DP[i] = (DP[i - 2] * 4 - DP[i - 4] % 1000000007) % 1000000007
    return DP[n] % 1000000007