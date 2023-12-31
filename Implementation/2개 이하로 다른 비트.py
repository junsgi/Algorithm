# https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2:
            bi = ["0"] + list(bin(i)[2:])
            for i in range(len(bi) - 2, -1, -1):
                if bi[i] == '0':
                    bi[i], bi[i + 1] = bi[i + 1], bi[i]
                    break
            answer.append(int("".join(bi), 2))
        else:
            answer.append(i + 1)
    return answer

print(solution([2, 7]))

"""
0111
1011
"""