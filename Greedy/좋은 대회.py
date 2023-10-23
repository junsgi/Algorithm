# https://www.acmicpc.net/problem/14610
# 반례 못 찾음
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ze = False
x = [1e9] * m # 각 문제가 풀렸는지
y = 0 # 참가자별 확인하지 못한 문제 개수
ans = "YES"
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0 or a[0] == m: 
        ze = True
        continue

    y += a[0] - a[1:].count(1)

    for j in range(m):
        if a[j + 1] != 0:
            if x[j] == 1e9:
                x[j] = a[j + 1]
            elif x[j] == -1 and a[j + 1] == 1:
                x[j] = 1
if ze: 
    ans = "NO"
if 1e9 in x : 
    ans = "NO"
if x.count(-1) > y:
    ans = "NO"

print(ans)
"""
모든 참가자가 같은 문제를 틀렸을 때
4 5
1 1 0 0 0 -1
2 1 0 1 0 -1
3 1 0 -1 -1 -1
4 1 1 -1 -1 -1



5 7
1 0 0 1 0 0 -1 -1
2 1 0 0 0 1 -1 -1
3 1 0 1 0 -1 -1 -1
3 1 1 1 0 -1 -1 -1
4 1 1 1 -1 -1 -1 -1

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
3 3
2 0 -1 -1
1 0 0 -1
1 -1 -1 -1

3 3
1 0 -1 -1
1 0 -1 -1
1 0 -1 -1

3 3
1 1 -1 -1
1 1 -1 -1
1 1 -1 -1

3 3
2 -1 -1 -1 
2 0 -1 -1
2 0 0 -1




3 3
2 0 -1 -1 
1 0 -1 1
1 0 0 1


3 3
2 1 1 -1
1 0 1 -1
1 1 0 -1
"""