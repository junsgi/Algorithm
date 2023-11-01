 # https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    answer = []
    stk = []
    for i in range(len(plans)):
        h, s = plans[i][1].split(":")
        plans[i][1] = int(h) * 60 + int(s)
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x : x[1])


    for i in range(1, len(plans)):
        before = plans[i - 1]
        # 인터럽트라면
        if before[1] < plans[i][1] < before[1] + before[2]:
            before[2] -= plans[i][1] - before[1]
            stk.append(before)
        # 작업이 마치는 동시에 시작한다면
        elif before[1] + before[2] == plans[i][1]:
            answer.append(before[0])
        else:
            answer.append(before[0])
            before[1] += before[2] # 이전 작업이 끝났으므로 현재 시간 처리
            while stk:
                value = stk.pop()
                if before[1] + value[2] <= plans[i][1]:
                    answer.append(value[0])
                    before[1] += value[2]
                else:
                    value[2] -= plans[i][1] - before[1]
                    stk.append(value)
                    break
                
    if len(answer) != len(plans) :
        stk.append(plans[-1])
        while stk: 
            answer.append(stk.pop()[0])
    return answer