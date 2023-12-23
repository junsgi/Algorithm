# https://www.acmicpc.net/problem/5052
n = int(input())
for _ in range(n):
    N = int(input())
    arr = sorted([input() for _ in range(N)])
    ans = "YES"
    for i in range(N - 1):
        if arr[i] == arr[i + 1][:len(arr[i])]:
            ans = "NO"
            break
    print(ans)            