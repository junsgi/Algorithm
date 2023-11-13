# https://www.acmicpc.net/problem/28284
from collections import deque
n, m = map(int, input().split())
cost = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
cost.sort(reverse=True)
arr.sort(key = lambda x : (x[0], x[1]))
taskQue = deque()
MAX = (arr[0][1] - arr[0][0] + 1) * cost[0]
MIN = (arr[0][1] - arr[0][0] + 1) * cost[-1]
taskQue.append(arr[0][1])
cur = 0
def solu():
    global MAX, MIN
    LEN = len(taskQue)
    for _ in range(LEN):
        

for i in range(1, len(arr)):
    st, ed = arr[i][0], arr[i][1]

    # 작업중에 들어왔다면
    if st <= taskQue[0]:
        # 이전 작업 끝나기 전 끝난다면
        if ed <= taskQue[0]:
            MAX += (ed - st + 1) * cost[len(taskQue)]
            MIN += (ed - st + 1) * cost[len(cost) - len(taskQue) - 1]
        else:
            MAX += (taskQue[0] - st + 1) * cost[len(taskQue)]
            MIN += (taskQue[0] - st + 1) * cost[len(cost) - len(taskQue) - 1]
            taskQue.append(ed)
            ted = taskQue.popleft()
            MAX += (ed - ted) * cost[len(taskQue) - 1]
            MIN += (ed - ted) * cost[len(cost) - len(taskQue)]
    else: # 앞 사람이 나갔다면
        if taskQue:
            taskQue.popleft()
        MAX += (ed - st + 1) * cost[len(taskQue)]
        MIN += (ed - st + 1) * cost[len(cost) - len(taskQue) - 1]
        taskQue.append(ed)
print(MIN, MAX)
