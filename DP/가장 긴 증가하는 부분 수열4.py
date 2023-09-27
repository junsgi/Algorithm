# https://www.acmicpc.net/problem/14002
def trac(idx):
    if PATH[idx] == -1:
        print(arr[idx], end = ' ')
        return
    trac(PATH[idx])
    print(arr[idx], end = ' ')
n = int(input())
arr = [0]
arr.extend(list(map(int, input().split())))
DP = [1] * (n + 1)
PATH = [-1] * (n + 1)
ans = 0
maxIdx = -1
for i in range(1, n + 1):
    num = arr[i]
    maxValue = 0
    for j in range(i - 1, 0, -1):
        if num > arr[j]:
            if maxValue < DP[j]:
                PATH[i] = j
                maxValue = DP[j]

    DP[i] = max(DP[i], maxValue + 1)

    if ans < DP[i]:
        maxIdx = i
        ans = DP[i]
print(ans)
trac(maxIdx)