# https://www.acmicpc.net/problem/28284
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cost = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
cost.sort(reverse=True)
arr.sort(key = lambda x : (x[0], x[1]))

taskQue = deque()
MAX = 0
MIN = 0

for st, ed in arr:
    # 사용중인 자리가 없거나 
    # 이용 시간이 큐에 있는 
    if not taskQue or taskQue[-1] < st:
        taskQue.clear()
        MAX += (ed - st + 1) * cost[0]
        MIN += (ed - st + 1) * cost[-1]
    else:
        LEN = len(taskQue)
        LEN2 = len(cost) - len(taskQue) - 1
        for _ in range(len(taskQue)):
            usingEd = taskQue.popleft()
            taskQue.append(usingEd)

            MAX += (usingEd - st + 1) * cost[LEN]
            MIN += (usingEd - st + 1) * cost[LEN2]
            if LEN == 0:
                break
            st = usingEd + 1
            
            LEN -= 1
            LEN2 += 1
        if st <= ed:
            MAX += (ed - st + 1) * cost[0]
            MIN += (ed - st + 1) * cost[-1]
    taskQue.append(ed)
        

print(MIN, MAX)