 # https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    answer = []
    stk = []
    for i in range(len(plans)):
        h, s = plans[i][1].split(":")
        plans[i][1] = int(h) * 60 + int(s)
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x : x[1])

    status = plans[0]
    cTime = plans[0][1]

    for i in range(1, len(plans)):
        endTime = cTime + status[2]
        # 인터럽트라면
        if endTime > plans[i][1]:
            status[2] -= plans[i][1] - cTime 
            stk.append(status)
        # 작업이 마치는 동시에 시작한다면
        elif endTime == plans[i][1]:
            answer.append(status[0])
        else:
            answer.append(status[0])
            while stk:
                value = stk.pop()
                if cTime + value[2] <= plans[i][1]:
                    answer.append(value[0])
                    cTime += value[2]
                else:
                    value[2] -= plans[i][1] - cTime
                    stk.append(value)
                    break

        status = plans[i]
        cTime = status[1]
    if len(answer) != len(plans) :
        stk.append(status)
    while stk: answer.append(stk.pop()[0])
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
print(solution(	[["a", "09:00", "10"], ["b", "09:10", "10"], ["c", "09:15", "10"], ["d", "09:30", "10"], ["e", "09:35", "10"]]))