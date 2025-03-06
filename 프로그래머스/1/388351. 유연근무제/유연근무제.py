def ntot(n):
    res = n % 10
    n //= 10
    res += (n % 10) * 10
    n //= 10
    res += n * 60
    return res
def solution(schedules, timelogs, startday):
    visit = [0] * (len(timelogs))
    answer = len(schedules)
    startday -= 1
    for i in range(len(schedules)):
        schedules[i] = ntot(schedules[i]) + 10
    
    for i in range(len(timelogs)):
        for j in range(7):
            timelogs[i][j] = ntot(timelogs[i][j])
    for j in range(7):
        if 5 <= (startday + j) % 7: continue
        for i in range(len(timelogs)):
            if timelogs[i][j] > schedules[i] and visit[i] == 0:
                answer -= 1
                visit[i] = 1
    return answer