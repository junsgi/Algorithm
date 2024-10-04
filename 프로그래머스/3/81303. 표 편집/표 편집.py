def up(k, cnt, linked):
    while cnt != 0 and linked[k][0] != -1:
        k = linked[k][0]
        cnt -= 1
    return k
def down(k, cnt, linked):
    while cnt != 0 and linked[k][1] != -1:
        k = linked[k][1]
        cnt -= 1
    return k
def solution(n, k, cmd):
    stk = []
    linked = {i : [i - 1, i + 1] for i in range(n)}
    linked[n - 1][1] = -1
    for c in cmd:
        if c[0] == "U": 
            k = up(k, int(c[2:]), linked)
        elif c[0] == "D": 
            k = down(k, int(c[2:]), linked)
        elif c == "C":
            stk.append(k)
            prev, next = linked[k]
            if next == -1:
                k = prev
            else:
                k = next
            if prev == -1:
                linked[next][0] = -1
            if next == -1:
                linked[prev][1] = -1
            if next != -1 and prev != -1:
                linked[prev][1] = next
                linked[next][0] = prev
        else:
            re = stk.pop()
            prev, cur, next = linked[re][0], re, linked[re][1]
            if prev == -1:
                linked[next][0] = cur
            elif next == -1:
                linked[prev][1] = cur
            else:
                linked[next][0] = cur
                linked[prev][1] = cur
    while 1:
        if linked[k][0] == -1:
            break
        k = linked[k][0]
    answer = ["X"] * n
    while k != -1:
        answer[k] = "O"
        k = linked[k][1]
    return ''.join(answer)

