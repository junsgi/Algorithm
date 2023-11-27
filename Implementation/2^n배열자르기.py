# https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        x = i // n
        y = i % n
        if x <= y:
            answer.append(y + 1)
        else:
            answer.append(x + 1)
    return answer