# https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    answer = []
    stk = []
    for i in range(len(plans)):
        h, s = plans[i][1].split(":")
        plans[i][1] = int(h) * 60 + int(s)
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x : x[1])
    cur = plans[0][1]
    work = plans[0]
    i = 0
    for i in range(1, len(plans)):
        # 인터럽트라면
        if cur + work[2] > plans[i][1]:
            work[2] = work[2] - (cur - plans[i][1])
            stk.append(work)
            work = plans[i]
            cur = work[1]
        # 새 작업을 시작할 수 있으면
        elif cur + work[2] < plans[i][1]:
            while stk:
                value = stk.pop()
                if cur + value[2] > plans[i][1]:
                    value[2] = value[2] - (plans[i][1] - cur)
                    stk.append(value)
                    cur = plans[i][1]
                    break
                else:
                    answer.append(value[0])
                    cur = value[1] + value[2]
            work = plans[i]
            cur = work[1]
        else:
            answer.append(work[0])
            cur = plans[i][1]
            work = plans[i]
        
    return answer

(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))