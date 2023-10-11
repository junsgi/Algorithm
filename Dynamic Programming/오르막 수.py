# https://www.acmicpc.net/problem/11057
n = int(input())
DP = [[0] * 10 for _ in range(n + 1)]
DP[0] = [1] * 10
for i in range(1, n + 1):
    DP[i][0] = 1
    for j in range(1, 10):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
print(DP[n][-1])

#import sys
#sys.setrecursionlimit(1000**2)
#check = "0123456789"
#answer = []
#def rec(depth, idx, value):
#    global n
#    if depth == n:
#        answer.append(value)
#        return
#    for i in range(idx, 10):
#        rec(depth + 1, i, value + check[i])
#rec(0, 0, "")
#print(answer)
#print(len(answer))