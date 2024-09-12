# https://www.acmicpc.net/problem/1038
import sys
input = sys.stdin.readline
n = int(input().strip())
a = []
check = '9876543210'
def BACK(depth, idx, end, value):
    if depth == end :
        a.append(int(value))
        return
    for i in range(idx, 10):
        BACK(depth + 1, i + 1, end, value + str(check[i]))

for i in range(1, 11):
    BACK(0,0,i,"")

a.sort()
if n < len(a):
    print(a[n])
else:
    print(-1)