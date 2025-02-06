def solution(sticker):
    if len(sticker) == 1: return sticker[0]
    DP = [0] * (len(sticker))
    DP[1] = sticker[0]
    for i in range(2, len(DP)):
        DP[i] = max(sticker[i - 1] + DP[i - 2], DP[i - 1])
    answer = DP[-1]
    sticker.reverse()
    DP[1] = sticker[0]
    for i in range(2, len(DP)):
        DP[i] = max(sticker[i - 1] + DP[i - 2], DP[i - 1])
    answer = max(answer, DP[-1])
    return answer