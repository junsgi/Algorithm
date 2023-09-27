# https://www.acmicpc.net/problem/2812
n, m = map(int, input().split())
arr = list(input())
stk = []
for idx in range(n):
    if len(stk) == 0 or stk[-1] >= arr[idx]:
        stk.append(arr[idx])
    else:
        while True:
            if m == 0 or len(stk) == 0 or stk[-1] >= arr[idx]: break
            m -= 1
            stk.pop()
        stk.append(arr[idx])
print(''.join(stk[:len(stk) - m]))