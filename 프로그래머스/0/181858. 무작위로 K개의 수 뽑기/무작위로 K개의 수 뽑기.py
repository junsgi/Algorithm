def solution(arr, k):
    visit = [0] * 100_001
    answer = []
    for i in arr:
        if visit[i]: continue
        answer.append(i)
        if len(answer) == k:
            break
        visit[i] = 1
    else:
        while len(answer) != k: answer.append(-1)
    return answer