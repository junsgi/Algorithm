def solution(numbers):
    answer = []
    c = [0] * 201
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if c[numbers[i] + numbers[j]] == 0:
                c[numbers[i] + numbers[j]] = 1
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer