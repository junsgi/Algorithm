# https://www.acmicpc.net/problem/2011

n = "."
n = n + input()
if n[1] == '0':
    print(0)
    exit()

DP = [0] * (len(n) + 1)
DP[0] = 1
DP[1] = 1
for i in range(2, len(n)):
    num = int(n[i - 1] + n[i])
    if num == 0 : break

    if n[i] == '0': # 1의자리가 0이라면
        if num > 20 : break
        DP[i] = DP[i - 2]
    elif n[i - 1] == '0':
        DP[i] = DP[i - 1]
    else:
        if num <= 26:
            DP[i] = DP[i - 1] + DP[i - 2]
        else:
            DP[i] = DP[i - 1]
print(DP[len(n) - 1] % 1000000) 
