# https://school.programmers.co.kr/learn/courses/30/lessons/42888
from collections import deque
def solution(record):
    answer = []
    dic = {}
    operQue = deque()
    for r in record:
        t = r.split()
            
        if t[0] == "Enter":
            operQue.append([t[1], "E"])
            dic[t[1]] = t[2]
        if t[0] == "Leave":
            operQue.append([t[1], "L"])
        if t[0] == "Change":
            dic[t[1]] = t[2]
    
    while operQue:
        usr_id, comm = operQue.popleft()
        if comm == 'E':
            answer.append(f"{dic[usr_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{dic[usr_id]}님이 나갔습니다.")

    return answer