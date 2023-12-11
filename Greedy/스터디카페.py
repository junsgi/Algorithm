# https://www.acmicpc.net/problem/28284
from collections import defaultdict
n, m = map(int, input().split())
c = sorted(list(map(int, input().split())))
cost = [0]
cost2 = [0]
for i in range(n):
    cost.append(c[i] + cost[-1])
    cost2.append(c[n - i - 1] + cost2[-1])
dic = defaultdict(int)
for i in range(m):
    st, ed = map(int, input().split())
    dic[st] += 1
    dic[ed + 1] -= 1
temp = 0
arr = sorted(dic.keys())
ans = [0, 0]

for i in range(1, len(dic)):
    temp += dic[arr[i - 1]]
    ans[0] += (arr[i] - arr[i - 1]) * cost[temp]
    ans[1] += (arr[i] - arr[i - 1]) * cost2[temp]
print(*ans)