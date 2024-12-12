from collections import deque
def solution(rc, operations):
    N, M = len(rc), len(rc[0])
    l = deque([rc[i][0] for i in range(N)])
    r = deque([rc[i][M - 1] for i in range(N)])
    row = deque([deque(rc[i][1 : M - 1]) for i in range(N)])
    for i in operations:
        if i == "ShiftRow":
            l.appendleft(l.pop())
            row.appendleft(row.pop())
            r.appendleft(r.pop())
        else:
            row[0].appendleft(l.popleft())
            r.appendleft(row[0].pop())
            row[-1].append(r.pop())
            l.append(row[-1].popleft())
    answer = []
    while row:
        answer.append([l.popleft()] + list(row.popleft()) + [r.popleft()])
    return answer