# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = []
    score = ""
    bonus = 0
    option = 1
    
    for i in range(len(dartResult)):
        if not score or dartResult[i].isdigit():
            if bonus:
                if option == 2 and len(answer) > 0:
                    answer[-1] *= 2
                answer.append(int(score) ** bonus * option)
                score = ""
                bonus = 0
                option = 1
            score += dartResult[i]
        elif 'A' <= dartResult[i]:
            if dartResult[i] == 'S':
                bonus = 1
            elif dartResult[i] == 'D':
                bonus = 2
            elif dartResult[i] == 'T':
                bonus = 3
        else:
            if dartResult[i] == '*':
                option = 2
            elif dartResult[i] == '#':
                option = -1
            else:
                option = 1
    if option == 2 and i - 1 >= 0:
        answer[-1] *= 2
    answer.append(int(score) ** bonus * option)
    return sum(answer)
print(
    solution(	"1S2D*3T")
)