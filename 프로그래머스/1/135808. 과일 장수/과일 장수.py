def solution(k, m, score):
    answer = 0
    score.sort(reverse = 1 == 1)
    for i in range(0, len(score), m):
        if i + m > len(score): break
        answer += min(score[i:i + m])
    return answer * m