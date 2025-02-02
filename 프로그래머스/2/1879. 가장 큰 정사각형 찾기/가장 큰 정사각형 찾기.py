def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    DP = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1][j - 1]:
                DP[i][j] = 1
            if DP[i][j] and DP[i][j - 1] and DP[i - 1][j] and DP[i - 1][j - 1]:
                DP[i][j] = min(DP[i][j - 1], DP[i - 1][j], DP[i - 1][j - 1]) + 1
            answer = max(answer, DP[i][j] * DP[i][j])
    return answer