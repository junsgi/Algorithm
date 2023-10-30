# https://school.programmers.co.kr/learn/courses/30/lessons/17687

dic = {i : str(i) for i in range(10)}
for i in range(10, 16):
    dic[i] = chr(55 + i)
def change(n, num):
    result = ''
    while num:
        result += dic[num % n]
        num //= n
    return '0' if not result else result[::-1]

def solution(n, t, m, p):
    answer = ''
    game = '.'
    for i in range(t * m + 1):
        game += change(n, i)
    while t != 0:
        answer += game[p]
        t -= 1
        p += m
    return answer
print(solution(16, 1000, 100, 55))