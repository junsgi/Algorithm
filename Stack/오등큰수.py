# https://www.acmicpc.net/problem/17299
"""
1. 스택이 비었거나 스택의 top 요소의 빈도수보다 적은 값이 들어오면 스택에 쌓는다 (위치, 현재 요소값, 스택 top의 A수열 요소값)
2. 스택의 top 요소의 빈도수보다 많거나 같은 값이 들어오면 1번 조건에 만족할 때까지 Pop
"""
n = int(input())
arr = list(map(int, input().split()))
dic = {}
for value in arr:
    if value in dic:
        dic[value] += 1
    else:
        dic[value] = 1
stk = []
ans = [0] * n
for idx in range(n - 1, -1, -1):
    value = arr[idx]

    if not stk:
        stk.append((idx, value, 0))
    elif dic[stk[-1][1]] > dic[value]:
        stk.append((idx, value, stk[-1][1]))
    else:

        while True:
            if not stk or dic[stk[-1][1]] > dic[value]: break
            temp = stk.pop()
            ans[temp[0]] = temp[2]
        
        if not stk:
            stk.append((idx, value, 0))
        else:
            stk.append((idx, value, stk[-1][1]))

while stk:
    temp = stk.pop()
    ans[temp[0]] = temp[2]
for i in ans:
    print(i if i else -1, end = ' ')