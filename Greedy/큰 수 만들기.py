# https://www.acmicpc.net/problem/16496
n = int(input())
arr = list(input().split())
def func(a, b):
    idx = 0
    while len(a) != len(b):
        if a[idx] < b[idx]: return True
        idx += 1
        if idx == len(a) or idx == len(b):
            if len(a) < len(b):
                print(idx)  
                if a[0] < b[idx]:
                    return True
                else : return False
            else:
                return a[idx] < b[0]
    return a <= b


for i in range(n):
    for j in range(i, n - 1):
        if func(arr[j], arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(int("".join(arr)))