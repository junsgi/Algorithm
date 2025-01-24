def solution(alp, cop, problems):
    MAX = 0x7fffffff
    answer = MAX
    A, B = alp, cop
    for a, b, _, _, _ in problems:
        A = max(A, a)
        B = max(B, b)
    
    DP = [[MAX for _ in range(B + 1)] for __ in range(A + 1)]
    
    DP[alp][cop] = 0
    for i in range(alp, A + 1):
        for j in range(cop, B + 1):
            DP[min(A, i + 1)][j] = min(DP[min(A, i + 1)][j], DP[i][j] + 1)
            DP[i][min(B, j + 1)] = min(DP[i][min(B, j + 1)], DP[i][j] + 1)
            
            for a, b, c, d ,e in problems:
                if a > i or b > j: continue # 문제를 풀지 못한다면
                DP[min(A, i + c)][min(B, j + d)] = min(DP[min(A, i + c)][min(B, j + d)], DP[i][j] + e)
    return DP[A][B]
