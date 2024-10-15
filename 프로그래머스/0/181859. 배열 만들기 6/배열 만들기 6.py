def solution(arr):
    answer = []
    for i in arr:
        if not answer or answer[-1] != i:
            answer.append(i)
        else:
            answer.pop()
    if not answer: answer.append(-1)
    return answer