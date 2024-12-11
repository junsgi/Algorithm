def solution(s):
    answer = []
    for i in s:
        cnt = 0
        stk = []
        for j in i:
            if len(stk) < 2 or stk[-2] + stk[-1] + j != "110":
                stk.append(j)
            else:
                cnt += 1
                stk.pop()
                stk.pop()
        if len(stk) >= 3 and stk[-3] + stk[-2] + stk[-1] == "110":
            cnt += 1
            stk.pop()
            stk.pop()
            stk.pop()
        x110 = "110" * cnt
        t = ""
        while stk and stk[-1] != "0":
            t += stk.pop()

        answer.append("".join(stk) + x110 + t)
    return answer
