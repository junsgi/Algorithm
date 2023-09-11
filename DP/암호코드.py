n = "."
n = n + input()
if n[1] == '0':
    print(0)
    exit()

DP = [0] * 5001
DP[1] = 1
if int(n[1:3]) <= 26:
    DP[2] = 2
else:
    DP[2] = 1

for i in range(3, len(n)):
    num = int(n[i-1] + n[i])
    if 0 < num <= 26:
        DP[i] = DP[i - 2] + DP[i - 1]
    else:
        if n[i] == '0':
            print(0)
            exit()
        DP[i] = DP[i - 1]
print(DP[len(n) - 1] % 1000000) 
