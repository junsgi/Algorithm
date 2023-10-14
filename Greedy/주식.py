# https://www.acmicpc.net/problem/11501
n = int(input())
for _ in range(n):
    T = int(input())
    stock = list(map(int, input().split()))[::-1]
    result = 0
    maxValue = stock[0]
    for i in range(1, T):
        if maxValue >= stock[i]:
            result += maxValue - stock[i]
        else:
            maxValue = stock[i]
    print(result)
