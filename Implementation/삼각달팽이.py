# https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    snail = [[0] * i for i in range(1, n + 1)]
    dire = [[1, 0], [0, 1], [-1, -1]]
    
    return answer