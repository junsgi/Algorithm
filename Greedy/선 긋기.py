# https://www.acmicpc.net/problem/2170
import sys
input = sys.stdin.readline
n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
if n == 1:
    print(line[0][1] - line[0][0])
    exit()
line.sort(key=lambda x : (x[0], x[1]))
st = line[0][0]
ed = line[0][1]
ans = 0
for x, y in line[1:]:
    if x <= ed:
        ed = max(ed, y)
    else:
        ans += ed - st
        st, ed = x, y
print(ans + (ed - st))