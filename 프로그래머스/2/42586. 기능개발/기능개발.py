def solution(progresses, speeds):
    answer = []
    t = 100 - progresses[0]
    t = (t // speeds[0]) + (1 if t % speeds[0] else 0)
    cnt = 1
    for i in range(1, len(speeds)):
        if progresses[i] + speeds[i] * t >= 100:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            temp = 100 - (progresses[i] + speeds[i] * t)
            t += (temp // speeds[i]) + (1 if temp % speeds[i] else 0)
    answer.append(cnt)
    return answer
# 5, 10, 1, 1, 20