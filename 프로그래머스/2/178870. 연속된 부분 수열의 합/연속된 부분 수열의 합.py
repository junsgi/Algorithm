def solution(sequence, k):
    answer = [0, 0x7fffffff]
    DP = [0]
    for i in sequence:
        DP.append(DP[-1] + i)
    left, right = 1, 1
    while right < len(DP):
        SUM = DP[right] - DP[left - 1]
        if SUM == k:
            if answer[1] - answer[0] > right - left or \
                answer[1] - answer[0] == right - left and answer[0] > left:
                answer[0], answer[1] = left - 1, right - 1
            right += 1
        elif SUM < k:
            right += 1
        else:
            left += 1
    return answer