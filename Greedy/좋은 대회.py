# https://www.acmicpc.net/problem/14610
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ze = False
x = [-999] * m
y = []
z = []
ans = "YES"
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0 or a[0] == m: 
        ze = True
    cnt = 0
    for j in range(1, m + 1):
        if a[j] == 1:
            cnt += 1
            x[j - 1] = 1
        if x[j - 1] == -999 and a[j] == -1:
            x[j - 1] = -1
    y.append(a[0] - cnt)

# 참여자 중 0점이 있을 때 (1번 조건 위반)
if ze: 
    print("누가 다 풀었거나, 0점일 때")
    ans = "NO"

# 모든 참가자가 같은 문제를 틀렸을 때 (2번 조건 위반)
if -999 in x : 
    print("모든 참가자가 같은 문제를 틀렸을 때")
    ans = "NO"

# 모든 문제가 한 명 이상의 참가자에게 풀리지 않았을 때
if x.count(-1) > sum(y): 
    print(x)
    print(y)
    print("모든 문제가 한 명 이상의 참가자에게 풀리지 않았을 때")
    ans = "NO"

print(ans)

"""
모든 참가자가 같은 문제를 틀렸을 때
5 3
1 0 -1 -1
1 0 -1 -1
1 0 -1 -1
1 0 -1 -1
1 0 -1 -1

3 7
4 1 1 1 -1 -1 -1 -1
3 1 1 0 0 -1 1 -1  
3 1 -1 1 0 -1 -1 -1
No

3 7
4 1 1 1 -1 -1 -1 -1
4 1 1 0 0 1 1 -1  
3 1 -1 1 0 0 -1 -1
YES

4 5
4 1 -1 -1 -1 -1
3 1 0 -1 -1 -1
2 1 0 1 0 -1
1 1 0 0 0 -1

4 5
4 1 -1 -1 -1 -1
3 1 1 -1 -1 -1
2 1 0 1 0 -1
1 1 0 0 0 -1

4 5
4 1 1 1 -1 -1
3 1 1 -1 -1 -1
2 1 0 1 0 -1
1 1 0 0 0 -1

4 5
4 1 1 1 -1 -1
3 1 1 1 -1 -1
2 1 0 1 0 -1
1 1 0 0 0 -1
"""