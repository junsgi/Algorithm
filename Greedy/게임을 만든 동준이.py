# https://www.acmicpc.net/problem/2847
n = int(input())
answer = 0
arr = []
for i in range(n):
    arr.append(int(input()))
    for j in range(i - 1, -1, -1):
        if arr[j] >= arr[j + 1]:
            answer += arr[j] - arr[j + 1] + 1
            arr[j] = arr[j + 1] - 1

print(answer)