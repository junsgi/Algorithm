# https://www.acmicpc.net/problem/16496
n = int(input())
arr = list(input().split())
def func(a, b): return a + b < b + a
for i in range(n):
    for j in range(n - i - 1):
        if func(arr[j], arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(int("".join(arr)))


"""
2
363 363361
ans : 363363361

2
373 3733
ans : 3733733

2
323 3233
ans : 3233323

2
378 3788
ans : 3788378

2
372 3722
ans : 3723722
    
3
10 100 1004
ans : 101004100
"""