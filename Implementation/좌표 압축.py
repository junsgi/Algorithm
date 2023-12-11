# https://www.acmicpc.net/problem/18870
n = int(input())
arr = []
ans = [0] * n
idx = 0
for v in map(int, input().split()):
    arr.append([v, idx])
    idx += 1
arr.sort(key = lambda x : x[0])
idx = 0
for i in range(1, n):
    if arr[i - 1][0] != arr[i][0]:
        idx += 1
    ans[arr[i][1]] = idx
print(*ans)