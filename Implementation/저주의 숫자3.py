# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def solution(n):
    answer = [0]
    num = 1
    def check(number):
        while number:
            t = number % 10
            if t != 0 and t == 3:
                return False
            number //= 10
        return True
    
    while len(answer) != n + 1:
        if num % 3 and check(num) :
            answer.append(num)
        num += 1
    return answer[n]