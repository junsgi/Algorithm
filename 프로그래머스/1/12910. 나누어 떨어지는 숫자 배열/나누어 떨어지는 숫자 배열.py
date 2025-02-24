def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if not answer: answer = [-1]
    return answer