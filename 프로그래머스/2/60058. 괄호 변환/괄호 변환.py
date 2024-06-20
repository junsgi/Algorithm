def isRight(p):
    res = 0
    for i in p:
        if i == '(': res += 1
        else: 
            res -= 1
            if res < 0: return False
    return res == 0
def div(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == '(': l += 1
        else: r += 1
        
        if l + r > 0 and l == r:
            return p[: i + 1], "" if i + 1 == len(p) else p[i + 1 :]
def rec(p):
    if not p : 
        return ""
    
    u, v = div(p)
    if isRight(u):
        return u + rec(v)
    else :
        res = ""
        for s in u[1:len(u) - 1]:
            if s == ')': res += "("
            else: res += ")"
        return "(" + rec(v) + ")" + res
        
    
def solution(p):
    return rec(p)