# https://www.acmicpc.net/problem/1343
x = input()
ans = ""
st = 0
ed = 0
while st != len(x):
    if x[st] == '.':
        ans += '.'
        st += 1
    else:
        ed = st + 1
        while ed < len(x) and x[ed] != '.':
            ed += 1
        length = ed - st
        if length % 2 != 0:
            ans = '-1'
            break
        ans += 'AAAA' * (length // 4)
        ans += 'BB' * (length % 4 // 2)
        st = ed
print(ans)