def solution(cards):
    cards = list(map(lambda x : x - 1, cards))
    answer = []
    check = [0] * len(cards)
    for i in range(len(cards)):
        if check[i]: continue
        check[i] = 1
        node = cards[i]
        cnt = 1
        while not check[node]:
            cnt += 1
            check[node] = 1
            node = cards[node]
        answer.append(cnt)
    if len(answer) == 1:
        return 0
    answer.sort()
    return answer[-1] * answer[-2]