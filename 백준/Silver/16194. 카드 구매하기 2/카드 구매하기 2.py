n = int(input())
arr = tuple(map(int, input().split()))
DP = [0] * (n + 1)
DP[1] = arr[0]
for i in range(2, n + 1):
    DP[i] = arr[i - 1]
    for j in range(1, i):
        DP[i] = min(DP[i], DP[i-j] + DP[j])
print(DP[n])