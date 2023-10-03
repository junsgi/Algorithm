# https://www.acmicpc.net/problem/1253
n = int(input())
minus = []
plus = []
arr = list(map(int, input().split()))
for num in arr:
    if num < 0:
        minus.append(num)
    elif num > 0:
        plus.append(num)
    else:
        plus.append(num)
        minus.append(num)
print(minus)
print(plus)