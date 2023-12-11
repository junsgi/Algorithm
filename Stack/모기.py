# https://www.acmicpc.net/problem/20440
from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for i in range(n):
    st, ed = map(int, input().split())
    dic[st] += 1
    dic[ed] -= 1
ans = [0, 0, 0]
temp = 0
swi = False
for k in sorted(dic.keys()):
    temp += dic[k]
    if temp > ans[0]:
        ans[0] = temp
        ans[1] = k
        swi = True
    elif temp < ans[0] and temp - dic[k] == ans[0] and swi:
        ans[2] = k
        swi = False
print(ans[0])
print(ans[1], ans[2])