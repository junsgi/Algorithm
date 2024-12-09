def solution(topping):
    answer = 0
    check = set()
    asc = []
    cnt = 0
    for i in topping:
        if i not in check:
            cnt += 1
        check.add(i)
        asc.append(cnt)
    check.clear()
    desc = [0] * len(topping)
    cnt = 0
    for i in range(len(topping) - 1, -1, -1):
        if topping[i] not in check:
            cnt += 1
        check.add(topping[i])
        desc[i] = cnt
    for i in range(len(asc) - 1):
        if asc[i] == desc[i + 1]:
            answer += 1
    
    return answer