def solution(array):
    answer = 0
    while array:
        n = array.pop()
        while n :
            if n % 10 == 7: answer += 1
            n //= 10
    
    return answer