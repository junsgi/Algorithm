def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    x, y, z = 0, 0, 0
    res = [[0, 1], [0, 2], [0, 3]]
    for i in range(len(answers)):
        if a1[x % 5] == answers[i]:
            res[0][0] += 1
        if a2[y % 8] == answers[i]:
            res[1][0] += 1
        if a3[z % 10] == answers[i]:
            res[2][0] += 1
        x += 1
        y += 1
        z += 1
    res.sort(key = lambda x : (-x[0], x[1]))
    answer.append(res[0][1])
    for i in range(1, 3):
        if res[i - 1][0] != res[i][0]:
            break
        answer.append(res[i][1])
    return answer