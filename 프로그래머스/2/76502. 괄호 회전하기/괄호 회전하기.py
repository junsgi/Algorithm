def solution(s):
    answer = 0
    MOD = len(s)
    def check(start):
        stk = []
        o = lambda x : x == "[" or x == "{" or x == "("
        c = lambda x, y : x == "[" and y == "]" or x == "{" and y == "}" or x == "(" and y == ")"
        for i in range(len(s)):
            idx = (start + i) % MOD
            if not stk or o(s[idx]):
                stk.append(s[idx])
            else:
                if not (stk and c(stk[-1], s[idx])):
                    return False
                stk.pop()
        if stk: return False
        return True
    for i in range(len(s) - 1):
        if check(i): answer += 1
    return answer