# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations
def solution(expression):
    answer = 0
    prio = {}
    for value in expression:
        if not value.isdigit() and value not in prio:
            prio[value] = -1
    numStk = []
    operStk = []
    for per in permutations(prio.keys(), len(prio)):
        # 숫자가 높을수록 순위가 높다
        rank = len(prio)
        for p in per:
            prio[p] = rank
            rank -= 1
        num = ""
        for value in expression:
            if value.isdigit():
                num += value
            else:
                numStk.append(int(num))
                num = ""

                if not operStk or prio[operStk[-1]] < prio[value]:
                    operStk.append(value)
                else:
                    calcul = 0
                    num1 = numStk.pop()
                    while True:
                        if len(operStk) == 0 or prio[operStk[-1]] < prio[value]:
                            break
                        num2 = numStk.pop()
                        oper = operStk.pop()
                        if oper == '+':
                            calcul = num2 + num1
                        elif oper == '-':
                            calcul = num2 - num1
                        elif oper == '*':
                            calcul = num2 * num1
                        
                        num1 = calcul
                        calcul = 0
                    numStk.append(num1)
                    operStk.append(value)
        calcul = 0
        num1 = int(num)
        while len(operStk) != 0:
            num2 = numStk.pop()
            oper = operStk.pop()
            if oper == '+':
                calcul = num2 + num1
            elif oper == '-':
                calcul = num2 - num1
            elif oper == '*':
                calcul = num2 * num1
            num1 = calcul
            calcul = 0
        answer = max(answer, abs(num1))
    return answer