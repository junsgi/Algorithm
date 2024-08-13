DP = [1] * 251
DP[2] = 3
for i in range(3, 251):
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 2]

while True:
    try:
        n = int(input())
        print(DP[n])
    except Exception as e:
        break