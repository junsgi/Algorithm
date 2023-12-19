# https://www.acmicpc.net/problem/1208
from collections import defaultdict
n, target = map(int, input().split())
arr = list(map(int, input().split()))
# 없는 값에 대해선 0으로 자동 대체
dic = defaultdict(int)
answer = 0
def BACK(idx, end, res, status):
    global answer, n, target
    if idx == end:
        if status:
            # 배열의 절반 부분에 대한 부분 수열을 모두 구함.
            dic[res] += 1
        else:
            # 왼쪽 부분 수열의 값 + res = target일때 정답임
            # 왼쪽 부분 수열의 값은 모두 딕셔너리에 저장되어 있으므로
            # 왼쪽 부분 수열의 값 = target - res로 찾는다
            answer += dic[target - res]
        return
    BACK(idx + 1, end, res + arr[idx], status)
    BACK(idx + 1, end, res, status)

BACK(0, n // 2, 0, True)
BACK(n // 2, n, 0, False)
if not target: answer -= 1
print(answer)