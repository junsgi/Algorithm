import sys
input = sys.stdin.readline
answer = set()
def check(res):
    row = False
    col = False
    rx = res[2] != '.' and res[2] == res[4] and res[4] == res[6]
    lx = res[0] != '.' and res[0] == res[4] and res[4] == res[8]
    for i in range(3):
        if res[i * 3] != '.' and res[i * 3] == res[i * 3 + 1] and res[i * 3 + 1] == res[i * 3 + 2]:
            row = True
        if res[i] != '.' and res[i] == res[i + 3] and res[i + 3] == res[i + 6]:
            col = True
    return row or col or rx or lx
def p(depth, res, O, X, before):
    if O > X or abs(O - X) > 1: return
    if check(res):
        answer.add("".join(res))
        return
    if depth == 9:
        if res.count(".") == 0:
            answer.add("".join(res))
        return
    for i in range(9):
        if res[i] != '.': continue
        if before == "X":
            res[i] = "O"
            p(depth + 1, res, O + 1, X, "O")
        else:
            res[i] = "X"
            p(depth + 1, res, O, X + 1, "X")

        res[i] = '.'
    
p(0, ['.'] * 9, 0, 0, "O")
n = None
while (n := input().strip()) != "end":
    if n in answer:
        print("valid")
    else:
        print("invalid")