def solution(name, yearning, photo):
    answer = []
    for p in photo:
        t = 0
        for i in range(len(name)):
            if name[i] in p:
                t += yearning[i]
        answer.append(t)
    return answer