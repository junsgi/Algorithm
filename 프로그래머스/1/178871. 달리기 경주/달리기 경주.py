def solution(players, callings):
    answer = []
    linked = {i:[None, None] for i in players}
    for i in range(len(players)):
        n = players[i]
        if i - 1 >= 0:
            linked[n][0] = players[i - 1]
        if i + 1 < len(players):
            linked[n][1] = players[i + 1]
    head = players[0]
    for i in callings:
        left = linked[i][0]
        cur = i
        if not left: continue
        nl, nr = linked[i]
        tl, ty = linked[linked[i][0]]
        
        linked[cur][0] = linked[left][0]
        linked[cur][1] = left
        if tl:
            linked[tl][1] = cur
        
        linked[left][0] = cur
        linked[left][1] = nr
        if nr:
            linked[nr][0] = left
        
        if not linked[cur][0]:
            head = cur
    while head:
        answer.append(head)
        head = linked[head][1]
    return answer