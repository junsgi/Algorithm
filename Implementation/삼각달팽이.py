# https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    snail = [[0] * i for i in range(1, n + 1)]
    dire = [[1, 0], [0, 1], [-1, -1]]
    x, y = 0, 0
    limit = [n, n, [0, 0]]
    value = 1
    zero = (1 + n) * n // 2
    while zero != 0:
        for i in range(3):
            while zero != 0:
                snail[x][y] = value
                zero -= 1
                value += 1
                tx, ty = x + dire[i][0], y + dire[i][1]
                if i == 0 and tx == limit[i] : 
                    y += 1
                    break
                elif i == 1 and ty >= limit[i] :
                    x -= 1
                    y -= 1
                    break
                elif i == 2 and tx == limit[i][0] and ty == limit[i][1]:
                    x += 1
                    break
                x = tx
                y = ty
            if zero == 0:break
            
        limit[0] -= 1
        limit[1] -= 2
        limit[2][0] += 2
        limit[2][1] += 1
    
    for i in range(n):
        answer.extend(snail[i])
    
    return answer
solution(6)