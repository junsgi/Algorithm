def solution(sequence):
    answer = -50_000_000_001
    DP = [[answer] * (len(sequence) + 1) for _ in range(2)]
    k = -1
    for i in range(1, len(sequence) + 1):
        t = sequence[i - 1]
        DP[0][i] = t * k
        DP[1][i] = t * -k
        
        if DP[0][i] < DP[0][i - 1] + DP[0][i]:
            DP[0][i] += DP[0][i - 1]
        if DP[1][i] < DP[1][i - 1] + DP[1][i]:
            DP[1][i] += DP[1][i - 1]
        k = -k
        answer = max(answer, max(DP[0][i], DP[1][i]))
    return answer