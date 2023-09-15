# https://www.acmicpc.net/problem/1449
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 1
st = 0
ed = 1
while ed < n:
    if a[ed] - a[st] + 1 <= m:
        ed += 1
    else:
        ans += 1
        st = ed
        ed += 1
print(ans)
"""
10 5                                                                                                              승__.py"
1 4 6 11 17 26 31 34 35 70
"""