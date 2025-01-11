def solution(order):
    answer = 0
    i = 0
    stk = []
    for n in range(1, len(order) + 1):
        stk.append(n)
        while stk and i < len(order) and stk[-1] == order[i]:
            answer += 1
            stk.pop()
            i += 1
    return answer