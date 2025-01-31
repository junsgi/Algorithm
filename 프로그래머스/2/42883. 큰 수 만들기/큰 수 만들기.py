def solution(number, k):
    stk = []
    idx = 0
    while k and idx < len(number):
        if not stk or stk[-1] >= number[idx]:
            stk.append(number[idx])
        else:
            while k and stk and stk[-1] < number[idx]:
                stk.pop()
                k -= 1
            stk.append(number[idx])
        idx += 1
        if k == 0:
            break
    if k:
        stk = stk[:len(stk) - k]
    else:
        for i in range(idx, len(number)):
            stk.append(number[i])
    return "".join(stk)
