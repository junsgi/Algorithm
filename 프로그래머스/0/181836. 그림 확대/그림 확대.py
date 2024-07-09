def solution(picture, k):
    answer = []
    for p in picture:
        temp = ""
        for s in p:
            temp += s * k
        for _ in range(k):
            answer.append(temp)
    return answer