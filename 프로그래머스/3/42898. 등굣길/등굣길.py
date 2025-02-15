def solution(m, n, puddles):
    MOD = 1_000_000_007
    DP = [[0] * (m + 1) for _ in range(n + 1)]
    DP[1][1] = 1
    for a, b in puddles:
        DP[b][a] = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if DP[i][j] == -1: continue
            if DP[i - 1][j] != -1:
                DP[i][j] = DP[i][j] % MOD + DP[i - 1][j] % MOD
            if DP[i][j - 1] != -1:
                DP[i][j] = DP[i][j] % MOD + DP[i][j - 1] % MOD
            DP[i][j] %= MOD
    for i in DP:
        print(i)
    return DP[n][m] % MOD