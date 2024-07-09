def solution(num, total):
    answer = [i + (total // num - ((num + 1) // 2)) for i in range(1, num + 1)]
    
    return answer
# [i + ((t // n - n + 1) // 2) for i in range(1, num + 1)]