def solution(money):
    answer = 0
    LEN = len(money)
    DP = [[0] * LEN for _ in range(2)]
    DP[0][1] = money[1]
    DP[0][2] = max(DP[0][1], money[2])
    
    for i in range(3, LEN):
        DP[0][i] = max(money[i] + max(DP[0][i - 2], DP[0][i - 3]), DP[0][i - 1])
    DP[1][LEN - 2] = money[LEN - 2]
    DP[1][LEN - 3] = max(DP[1][LEN - 2], money[LEN - 3])
    for i in range(LEN - 4, -1, -1):
        DP[1][i] = max(money[i] + max(DP[1][i + 2], DP[1][i + 3]), DP[1][i + 1])
    return max(DP[0][-1], DP[1][0])