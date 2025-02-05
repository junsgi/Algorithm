def solution(survey, choices):
    answer = ''
    d = {b : a for a, b in enumerate(["R", 'T', 'C', 'F', 'J', 'M', 'A', 'N'])}
    r = {a : b for a, b in enumerate(["R", 'T', 'C', 'F', 'J', 'M', 'A', 'N'])}
    arr = [0] * 8
    cost = [i for i in range(-4, 4)]
    for i in range(len(survey)):
        da, a = d[survey[i][0]], d[survey[i][1]]
        arr[da] -= cost[choices[i]]
        arr[a] += cost[choices[i]]
    for i in range(1, 8, 2):
        if arr[i - 1] < arr[i]:
            answer += r[i]
        elif arr[i - 1] > arr[i]:
            answer += r[i - 1]
        else:
            if r[i] < r[i - 1]:
                answer += r[i]
            else:
                answer += r[i - 1]
    return answer