# https://school.programmers.co.kr/learn/courses/30/lessons/17678
"""
1. 전부 분으로 계산 후 내림차순 정렬
2. 버스 시간을 미리 구해놓았으므로 n - 1번만 돌면 가장 늦게 탈 수 있는 버스 시간이 나옴
3. 탈 수 있는 사람보다 타야할 사람이 더 많다면
    - 막차 시간에 맞춰서 타는 사람이 있다면 그 사람보다 1분 일찍 도착
    - 
"""
def solution(n, t, m, timetable):
    answer = 0
    bus = 9 * 60
    for i in range(len(timetable)):
        h, mi = timetable[i].split(":")
        timetable[i] = (int(h) * 60) + int(mi)
    timetable.sort(reverse = True)

    for i in range(n - 1):
        for j in range(m):
            if timetable and timetable[-1] <= bus: 
                timetable.pop()
            else:
                break
        bus += t
        
    x = 0
    if len(timetable) >= m:
        x = len(timetable) - m
        if timetable[x] <= bus:
            answer = timetable[x] - 1
        else:
            answer = bus
    else:
        answer = bus
            
    return f"{answer//60:02d}:{answer%60:02d}"