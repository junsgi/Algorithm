def solution(mats, park):
    answer = -1
    n, m = len(park), len(park[0])
    DP = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if park[i][j] != "-1": continue
            DP[i + 1][j + 1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if DP[i][j] == 0: continue
            DP[i][j] = min(DP[i][j - 1], DP[i - 1][j - 1], DP[i - 1][j]) + 1
            if DP[i][j] in mats:
                answer = max(answer, DP[i][j])
    return answer