n = int(input())
arr = tuple(map(int, input().split()))
DP = [1] * n
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))