def solution(prices):
    answer = [0] * len(prices)
    stk = []
    for i in range(len(prices)):
        if not stk or stk[-1][0] <= prices[i]:
            stk.append((prices[i], i))
        else:
            while stk and stk[-1][0] > prices[i]:
                _, idx = stk.pop()
                answer[idx] = i - idx
            stk.append((prices[i], i))
    stk.pop()
    while stk:
        _, idx = stk.pop()
        answer[idx] = len(prices) - 1 - idx
    return answer