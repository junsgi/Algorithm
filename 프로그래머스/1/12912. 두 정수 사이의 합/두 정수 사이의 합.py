def solution(a, b):
    return (a + b) * (max(a, b) - min(a, b) + 1) // 2
