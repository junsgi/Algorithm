# https://www.acmicpc.net/problem/28284
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cost = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
LEN = 0
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
        taskQue.append(ed)
    else:
        LEN = len(taskQue)
        for _ in range(len(taskQue)):
            usingEd = taskQue.popleft()
            taskQue.append(usingEd)

            if LEN > 0:
                MAX += (usingEd - st + 1) * cost[LEN]
                MIN += (ed - st + 1) * cost[LEN]

                st = usingEd + 1
            else:
                MAX += (usingEd - st + 1) * cost[0]
                MIN += (ed - st + 1) * cost[-1]

                break
            LEN -= 1
        if st <= ed:
            MAX += (ed - st + 1) * cost[0]
            MIN += (ed - st + 1) * cost[-1]

print(MIN, MAX)