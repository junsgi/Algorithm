n = int(input())
arr = list(input())
DP = [9999999] * n
DP[0] = 0
d = {"J" : 0, "O" : 1, "B" : 2}
c = "J", "O", "B"
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if arr[j] == c[(d[arr[i]] + 1) % 3]:
            DP[i] = min(DP[i], DP[j] + (i - j) * (i - j)) 
if DP[-1] == 9999999:
    print(-1)
else:
    print(DP[-1])