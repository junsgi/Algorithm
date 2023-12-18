# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1])
    x = -1
    for a, b in targets:
        if x == -1 or x <= a:
            x = b
            answer += 1
    return answer