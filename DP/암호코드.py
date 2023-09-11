# https://www.acmicpc.net/problem/2011

n = "."
n = n + input()
if n[1] == '0':
    print(0)
    exit()

DP = [0] * (len(n) + 1)
DP[1] = 1
if len(n) > 2:
    if n[2] != '0' and int(n[1] + n[2]) <= 26:
        DP[2] = 2
    else:
        if n[2] == '0':
            n = ''
        DP[2] = 1

    idx = 3
    for i in range(3, len(n)):
        num = int(n[i - 1] + n[i])
        if num == 0: break
        if n[i] == '0':
            if num > 20 : break
            DP[i] = DP[i - 2]
        elif n[i - 1] == '0':
            DP[i] = DP[i - 1]
        else:
            if num <= 26:
                DP[i] = DP[i - 2] + DP[i - 1] % 1000000
            else:
                DP[i] = DP[i - 1]
            
print(DP[len(n) - 1] % 1000000) 
